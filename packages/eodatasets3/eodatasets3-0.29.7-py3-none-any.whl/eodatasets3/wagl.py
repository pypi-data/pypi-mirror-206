"""
Package WAGL HDF5 Outputs

This converts the HDF5 file (and sibling fmask/gqa files) into
GeoTIFFS (COGs) with datacube metadata using the DEA naming conventions
for files.
"""
import contextlib
import os
import re
import sys
from datetime import datetime, timedelta
from enum import Enum
from math import isnan
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple
from uuid import UUID

import attr
import numpy
import rasterio
from affine import Affine
from boltons.iterutils import PathAccessError, get_path
from click import secho
from rasterio import DatasetReader
from rasterio.crs import CRS
from rasterio.enums import Resampling

from eodatasets3 import DatasetAssembler, images, serialise, utils
from eodatasets3.images import GridSpec
from eodatasets3.model import DatasetDoc
from eodatasets3.properties import Eo3Interface
from eodatasets3.serialise import loads_yaml
from eodatasets3.ui import bool_style
from eodatasets3.utils import default_utc, flatten_dict

try:
    import h5py
except ImportError:
    sys.stderr.write(
        "eodatasets3 has not been installed with the wagl extras. \n"
        "    Try `pip install eodatasets3[wagl]\n"
    )
    raise

POSSIBLE_PRODUCTS = ("nbar", "nbart", "lambertian", "sbt")
DEFAULT_PRODUCTS = ("nbar", "nbart")

_THUMBNAILS = {
    "nbar": ("nbar:red", "nbar:green", "nbar:blue"),
    "nbart": ("nbart:red", "nbart:green", "nbart:blue"),
}

os.environ["CPL_ZIP_ENCODING"] = "UTF-8"

FILENAME_TIF_BAND = re.compile(
    r"(?P<prefix>(?:.*_)?)(?P<band_name>B[0-9][A0-9]|B[0-9]*|B[0-9a-zA-z]*)"
    r"(?P<extension>\....)"
)
PRODUCT_SUITE_FROM_GRANULE = re.compile("(L1[GTPCS]{1,2})")


class ProductMaturity(Enum):
    provisional = "provisional"
    stable = "stable"


def _find_h5_paths(h5_obj: h5py.Group, dataset_class: str = "") -> List[str]:
    """
    Find all objects in a h5 of the given class, returning their path.

    (class examples: IMAGE, TABLE. SCALAR)
    """
    items = []

    def _find(name, obj):
        if obj.attrs.get("CLASS") == dataset_class:
            items.append(name)

    h5_obj.visititems(_find)
    return items


def _unpack_products(
    p: DatasetAssembler, product_list: Iterable[str], h5group: h5py.Group
) -> None:
    """
    Unpack and package the NBAR and NBART products.
    """
    # listing of all datasets of IMAGE CLASS type
    img_paths = _find_h5_paths(h5group, "IMAGE")

    for product in product_list:
        with sub_product(product, p):
            for pathname in [p for p in img_paths if f"/{product.upper()}/" in p]:
                with do(f"Path {pathname!r}"):
                    dataset = h5group[pathname]
                    band_name = utils.normalise_band_name(dataset.attrs["alias"])
                    write_measurement_h5(
                        p,
                        f"{product}:{band_name}",
                        dataset,
                        overview_resampling=Resampling.average,
                        file_id=_file_id(dataset),
                    )

            if product in _THUMBNAILS:
                red, green, blue = _THUMBNAILS[product]
                with do(f"Thumbnailing {product}"):
                    p.write_thumbnail(
                        red,
                        green,
                        blue,
                        static_stretch=(1, 3000),
                        # Because of our strange sub-products and filename standards, we want the
                        # 'kind' to be included in the recorded thumbnail accessory metadata,
                        # but not in the filename.
                        # So we manually calculate a filename without the 'kind' field included.
                        kind=product,
                        path=p.names.thumbnail_filename(),
                    )


def write_measurement_h5(
    p: DatasetAssembler,
    full_name: str,
    g: h5py.Dataset,
    overviews=images.DEFAULT_OVERVIEWS,
    overview_resampling=Resampling.nearest,
    expand_valid_data=True,
    file_id: str = None,
):
    """
    Write a measurement by copying it from a hdf5 dataset.
    """
    if hasattr(g, "chunks"):
        data = g[:]
    else:
        data = g

    product_name, band_name = full_name.split(":")
    p.write_measurement_numpy(
        array=data,
        grid_spec=images.GridSpec(
            shape=g.shape,
            transform=Affine.from_gdal(*g.attrs["geotransform"]),
            crs=CRS.from_wkt(g.attrs["crs_wkt"]),
        ),
        nodata=g.attrs.get("no_data_value"),
        overviews=overviews,
        overview_resampling=overview_resampling,
        expand_valid_data=expand_valid_data,
        file_id=file_id,
        # Because of our strange sub-products and filename standards, we want the
        # product_name to be included in the recorded band metadata,
        # but not in its filename.
        # So we manually calculate a filename without the extra product name prefix.
        name=full_name,
        path=p.names.measurement_filename(band_name, "tif", file_id=file_id),
    )


def _file_id(dataset: h5py.Dataset) -> str:
    """
    Devise a file id for the given dataset (using its attributes)

    Eg. 'band01'
    """
    # What we have to work with:
    # >>> print(repr((dataset.attrs["band_id"], dataset.attrs["band_name"], dataset.attrs["alias"])))
    # ('1', 'BAND-1', 'Blue')

    band_name = dataset.attrs["band_id"]

    # A purely numeric id needs to be formatted 'band01' according to naming conventions.
    return utils.normalise_band_name(band_name)


def _unpack_observation_attributes(
    p: DatasetAssembler,
    res_grp: h5py.Group,
):
    """
    Unpack the angles + other supplementary datasets produced by wagl.
    Currently only the mode resolution group gets extracted.
    """

    def _write(section: str, dataset_names: Sequence[str]):
        """
        Write supplementary attributes as measurement.
        """
        for dataset_name in dataset_names:
            o = f"{section}/{dataset_name}"
            with do(f"Path {o!r} "):
                measurement_name = utils.normalise_band_name(dataset_name)
                write_measurement_h5(
                    p,
                    f"oa:{measurement_name}",
                    res_grp[o],
                    # We only use the product bands for valid data calc, not supplementary.
                    # According to Josh: Supplementary pixels outside of the product bounds are implicitly invalid.
                    expand_valid_data=False,
                    overviews=None,
                )

    _write(
        "SATELLITE-SOLAR",
        [
            "SATELLITE-VIEW",
            "SATELLITE-AZIMUTH",
            "SOLAR-ZENITH",
            "SOLAR-AZIMUTH",
            "RELATIVE-AZIMUTH",
            "TIME-DELTA",
        ],
    )
    _write("INCIDENT-ANGLES", ["INCIDENT-ANGLE", "AZIMUTHAL-INCIDENT"])
    _write("EXITING-ANGLES", ["EXITING-ANGLE", "AZIMUTHAL-EXITING"])
    _write("RELATIVE-SLOPE", ["RELATIVE-SLOPE"])
    _write("SHADOW-MASKS", ["COMBINED-TERRAIN-SHADOW"])


def get_oa_resolution_group(
    resolution_groups: Dict[tuple, h5py.Group],
    platform: str,
    oa_resolution: Optional[Tuple[float, float]],
) -> h5py.Group:
    # None specified? Figure out a default.

    if oa_resolution is None:
        # For Landsat, we only cared about packaging OA data for the "common"
        # bands (not panchromatic). So we always pick the higher resolution.
        if platform.startswith("landsat"):
            oa_resolution = max(resolution_groups.keys())
        elif platform.startswith("sentinel"):
            oa_resolution = (20.0, 20.0)
        else:
            raise NotImplementedError(
                f"Don't know how to choose a default OA resolution for platform {platform !r}"
            )

    res_grp = resolution_groups.get(oa_resolution)
    if res_grp is None:
        raise RuntimeError(
            f"Resolution {oa_resolution} not found in input. "
            f"Have resolutions {tuple(resolution_groups.keys())}"
        )

    return res_grp


def _create_contiguity(
    p: DatasetAssembler,
    product_list: Iterable[str],
    resolution_yx: Tuple[float, float],
    timedelta_product: str = "nbar",
    timedelta_data: numpy.ndarray = None,
):
    """
    Create the contiguity (all pixels valid) dataset.

    Write a contiguity mask file based on the intersection of valid data pixels across all
    bands from the input files.
    """
    for product in product_list:
        contiguity = None
        for grid, band_name, path in p.iter_measurement_paths():
            if not band_name.startswith(f"{product.lower()}:"):
                continue
            # Only our given res group (no pan band in Landsat)
            if grid.resolution_yx != resolution_yx:
                continue

            with rasterio.open(path) as ds:
                ds: DatasetReader
                if contiguity is None:
                    contiguity = numpy.ones((ds.height, ds.width), dtype="uint8")
                    geobox = GridSpec.from_rio(ds)
                elif ds.shape != contiguity.shape:
                    raise NotImplementedError(
                        "Contiguity from measurements of different shape"
                    )

                for band in ds.indexes:
                    contiguity &= ds.read(band) > 0

        if contiguity is None:
            secho(f"No images found for requested product {product}", fg="red")
            continue

        p.write_measurement_numpy(
            f"oa:{product.lower()}_contiguity",
            contiguity,
            geobox,
            nodata=255,
            overviews=None,
            expand_valid_data=False,
            # Because of our strange sub-products and filename standards, we want the
            # 'oa_' prefix to be included in the recorded band metadata,
            # but not in its filename.
            # So we manually calculate a filename without the extra prefix.
            path=p.names.measurement_filename(f"{product.lower()}_contiguity"),
        )

        # masking the timedelta_data with contiguity mask to get max and min timedelta within the NBAR product
        # footprint for Landsat sensor. For Sentinel sensor, it inherits from level 1 yaml file
        if timedelta_data is not None and product.lower() == timedelta_product:
            valid_timedelta_data = numpy.ma.masked_where(
                contiguity == 0, timedelta_data
            )

            def offset_from_center(v: numpy.datetime64):
                return p.datetime + timedelta(
                    microseconds=v.astype(float) * 1_000_000.0
                )

            p.datetime_range = (
                offset_from_center(numpy.ma.min(valid_timedelta_data)),
                offset_from_center(numpy.ma.max(valid_timedelta_data)),
            )


@contextlib.contextmanager
def do(name: str, heading=False, **fields):
    """
    Informational logging.

    TODO: move this to the cli. It shouldn't be part of library usage.
    """
    single_line = not heading

    def val(v: Any):
        if isinstance(v, bool):
            return bool_style(v)
        if isinstance(v, Path):
            return repr(str(v))
        return repr(v)

    if heading:
        name = f"\n{name}"
    fields = " ".join(f"{k}:{val(v)}" for k, v in fields.items())
    secho(f"{name} {fields} ", nl=not single_line, fg="blue" if heading else None)
    yield
    if single_line:
        secho("(done)")


@contextlib.contextmanager
def sub_product(name: str, p: Eo3Interface):
    """
    Set the product family temporarily within a block of code.

    This is done for sub-products that WAGL contains, which have
    a different 'family' in their filenames.
    """
    with do(f"Product {name}", heading=True):
        original_family = p.product_family
        # We delete first to show that we're deliberately changing the value (no 'overridding property" warning)
        del p.product_family
        p.product_family = name
        yield
        del p.product_family
        p.product_family = original_family


def _extract_reference_code(p: DatasetAssembler, granule: str) -> Optional[str]:
    matches = None
    if p.platform.startswith("landsat"):
        matches = re.match(r"L\w\d(?P<reference_code>\d{6}).*", granule)
    elif p.platform.startswith("sentinel-2"):
        matches = re.match(r".*_T(?P<reference_code>\d{1,2}[A-Z]{3})_.*", granule)

    if matches:
        [reference_code] = matches.groups()
        # TODO name properly
        return reference_code
    return None


@attr.s(auto_attribs=True)
class Granule:
    """
    A single granule in a hdf5 file, with optional corresponding fmask/gqa/etc files.

    You probably want to make one by using `Granule.for_path()`
    """

    name: str
    wagl_hdf5: Path
    wagl_metadata: Dict
    source_level1_metadata: Optional[DatasetDoc]

    fmask_doc: Optional[Dict] = None
    fmask_image: Optional[Path] = None
    s2cloudless_prob: Optional[Path] = None
    s2cloudless_mask: Optional[Path] = None
    s2cloudless_doc: Optional[Dict] = None
    gqa_doc: Optional[Dict] = None
    tesp_doc: Optional[Dict] = None

    @classmethod
    def for_path(
        cls,
        wagl_hdf5: Path,
        granule_names: Optional[Sequence[str]] = None,
        level1_metadata_path: Optional[Path] = None,
        fmask_image_path: Optional[Path] = None,
        fmask_doc_path: Optional[Path] = None,
        s2cloudless_prob_path: Optional[Path] = None,
        s2cloudless_mask_path: Optional[Path] = None,
        s2cloudless_doc_path: Optional[Path] = None,
        gqa_doc_path: Optional[Path] = None,
        tesp_doc_path: Optional[Path] = None,
        allow_missing_provenance: bool = False,
    ):
        """
        Create granules by scanning the given hdf5 file.

        Optionally specify additional files and level1 path.

        If they are not specified it look for them using WAGL's output naming conventions.
        :param allow_missing_provenance:
        """
        if not wagl_hdf5.exists():
            raise ValueError(f"Input hdf5 doesn't exist {wagl_hdf5}")

        with h5py.File(wagl_hdf5, "r") as fid:
            granule_names = granule_names or fid.keys()

            for granule_name in granule_names:
                if granule_name not in fid:
                    raise ValueError(
                        f"Granule {granule_name!r} not found in file {wagl_hdf5}"
                    )

                wagl_doc_field = get_path(fid, (granule_name, "METADATA", "CURRENT"))
                if not wagl_doc_field:
                    raise ValueError(
                        f"Granule contains no wagl metadata: {granule_name} in {wagl_hdf5}"
                    )

                [wagl_doc] = loads_yaml(wagl_doc_field[()])

                level1 = _load_level1_doc(
                    wagl_doc, level1_metadata_path, allow_missing_provenance
                )

                fmask_image_path = fmask_image_path or wagl_hdf5.with_name(
                    f"{granule_name}.fmask.img"
                )
                if not fmask_image_path.exists():
                    raise ValueError(f"No fmask image found at {fmask_image_path}")

                fmask_doc_path = fmask_doc_path or fmask_image_path.with_suffix(".yaml")
                if not fmask_doc_path.exists():
                    raise ValueError(f"No fmask found at {fmask_doc_path}")
                with fmask_doc_path.open("r") as fl:
                    [fmask_doc] = loads_yaml(fl)

                if "sentinel" in wagl_doc["source_datasets"]["platform_id"].lower():
                    s2cloudless_prob_path = (
                        s2cloudless_prob_path
                        or wagl_hdf5.with_name(f"{granule_name}.prob.s2cloudless.tif")
                    )
                    if not s2cloudless_prob_path.exists():
                        raise ValueError(
                            f"No s2cloudless probability image found at {s2cloudless_prob_path}"
                        )

                    s2cloudless_mask_path = (
                        s2cloudless_mask_path
                        or wagl_hdf5.with_name(f"{granule_name}.mask.s2cloudless.tif")
                    )
                    if not s2cloudless_mask_path.exists():
                        raise ValueError(
                            f"No s2cloudless mask image found at {s2cloudless_mask_path}"
                        )

                    s2cloudless_doc_path = s2cloudless_doc_path or wagl_hdf5.with_name(
                        f"{granule_name}.s2cloudless.yaml"
                    )
                    if not s2cloudless_doc_path.exists():
                        raise ValueError(
                            f"No s2cloudless metadata found at {s2cloudless_doc_path}"
                        )
                    with s2cloudless_doc_path.open("r") as fl:
                        [s2cloudless_doc] = loads_yaml(fl)
                else:
                    s2cloudless_prob_path = None
                    s2cloudless_mask_path = None
                    s2cloudless_doc = None

                gqa_doc_path = gqa_doc_path or wagl_hdf5.with_name(
                    f"{granule_name}.gqa.yaml"
                )
                if not gqa_doc_path.exists():
                    raise ValueError(f"No gqa found at {gqa_doc_path}")
                with gqa_doc_path.open("r") as fl:
                    [gqa_doc] = loads_yaml(fl)

                # Optional doc
                if tesp_doc_path:
                    # But if they gave us a path, we're strict about it existing.
                    if not tesp_doc_path.exists():
                        raise ValueError(
                            f"Supplied tesp doc path doesn't exist: {tesp_doc_path}"
                        )
                else:
                    tesp_doc_path = wagl_hdf5.with_name(f"{granule_name}.tesp.yaml")

                tesp_doc = None
                if tesp_doc_path.exists():
                    with tesp_doc_path.open("r") as fl:
                        [tesp_doc] = loads_yaml(fl)

                yield cls(
                    name=granule_name,
                    wagl_hdf5=wagl_hdf5,
                    wagl_metadata=wagl_doc,
                    source_level1_metadata=level1,
                    fmask_doc=fmask_doc,
                    fmask_image=fmask_image_path,
                    s2cloudless_prob=s2cloudless_prob_path,
                    s2cloudless_mask=s2cloudless_mask_path,
                    s2cloudless_doc=s2cloudless_doc,
                    gqa_doc=gqa_doc,
                    tesp_doc=tesp_doc,
                )


def _load_level1_doc(
    wagl_doc: Dict,
    user_specified_l1_path: Optional[Path] = None,
    allow_missing_provenance=False,
):
    if user_specified_l1_path:
        if not user_specified_l1_path.exists():
            raise ValueError(
                f"No level1 metadata found at given path {user_specified_l1_path}"
            )
        level1_path = user_specified_l1_path
    else:
        level1_path = Path(get_path(wagl_doc, ("source_datasets", "source_level1")))

    # If a directory, assume "<dirname>.odc-metadata.yaml"
    if level1_path.is_dir():
        metadata_path = level1_path / (level1_path.name + ".odc-metadata.yaml")
    # Otherwise it's a sibling file with ".odc-metadata.yaml" suffix
    else:
        if level1_path.suffix.lower() == ".yaml":
            metadata_path = level1_path
        else:
            metadata_path = level1_path.with_suffix(".odc-metadata.yaml")

    if not metadata_path.exists():
        if not allow_missing_provenance:
            raise ValueError(
                "No level1 found or provided. "
                f"WAGL said it was at path {str(level1_path)!r}. "
                "Which has no metadata doc we can find, and you didn't specify an alternative. "
                f"(allow_missing_provenance={allow_missing_provenance})"
            )
        return None
    return serialise.from_path(metadata_path)


def package_file(
    out_directory: Path,
    hdf_file: Path,
    included_products: Iterable[str] = DEFAULT_PRODUCTS,
    include_oa: bool = True,
) -> Dict[UUID, Path]:
    """
    Simple alternative to package().

    Takes a single HDF5 and infers other paths (gqa etc) via naming conventions.

    Returns a dictionary of the output datasets: Mapping UUID to the their metadata path.
    """

    out = {}
    for granule in Granule.for_path(hdf_file):
        dataset_id, metadata_path = package(
            out_directory,
            granule,
            included_products=included_products,
            include_oa=include_oa,
        )
        out[dataset_id] = metadata_path

    return out


def package(
    out_directory: Path,
    granule: Granule,
    *,
    product_maturity: ProductMaturity = ProductMaturity.stable,
    included_products: Iterable[str] = DEFAULT_PRODUCTS,
    include_oa: bool = True,
    oa_resolution: Optional[Tuple[float, float]] = None,
    contiguity_resolution: Optional[Tuple[float, float]] = None,
) -> Tuple[UUID, Path]:
    """
    Package an L2 product.

    :param include_oa:

    :param out_directory:
        The base directory for output datasets. A DEA-naming-conventions folder hierarchy
        will be created inside this folder.

    :param granule:
        Granule information. You probably want to make one with Granule.from_path()

    :param included_products:
        A list of imagery products to include in the package.
        Defaults to all products.

    :return:
        The dataset UUID and output metadata path
    """
    included_products = tuple(s.lower() for s in included_products)

    with h5py.File(granule.wagl_hdf5, "r") as fid:
        granule_group = fid[granule.name]

        wagl_doc = _read_wagl_metadata(granule_group)

        with DatasetAssembler(
            out_directory.absolute(),
            # WAGL stamps a good, random ID already.
            dataset_id=granule.wagl_metadata.get("id"),
            naming_conventions="dea_s2"
            if ("sentinel" in wagl_doc["source_datasets"]["platform_id"].lower())
            else "dea",
        ) as p:
            _apply_wagl_metadata(p, wagl_doc)

            # It's a GA ARD product.
            p.producer = "ga.gov.au"
            p.product_family = "ard"
            p.maturity = _determine_maturity(
                acq_date=p.datetime,
                processed=p.processed,
                wagl_doc=wagl_doc,
            )

            # We don't bother including product maturity if it's stable, for consistency with old datasets.
            # Stable is the assumed default.
            if product_maturity is not ProductMaturity.stable:
                p.product_maturity = product_maturity

            if granule.source_level1_metadata is not None:
                # For historical consistency: we want to use the instrument that the source L1 product
                # came from, not the instruments reported from the WAGL doc.
                #
                # Eg.
                #     Level 1 will say "OLI_TIRS", while wagl doc will say "OLI".
                #     Our current C3 products say "OLI_TIRS" so we need to stay consistent.
                #     (even though WAGL only *used* the OLI bands, it came from an OLI_TIRS observation)
                #
                # So delete our current wagl one, since we're adding a source dataset:
                if p.instrument is not None:
                    del p.properties["eo:instrument"]

                p.add_source_dataset(
                    granule.source_level1_metadata, auto_inherit_properties=True
                )
                # When level 1 is NRT, ARD is always NRT.
                if granule.source_level1_metadata.maturity == "nrt":
                    p.maturity = "nrt"

            org_collection_number = utils.get_collection_number(
                p.platform, p.producer, p.properties.get("landsat:collection_number")
            )

            p.dataset_version = f"{org_collection_number}.2.1"
            p.region_code = _extract_reference_code(p, granule.name)

            _read_gqa_doc(p, granule.gqa_doc)
            _read_fmask_doc(p, granule.fmask_doc)
            if granule.s2cloudless_doc:
                _read_s2cloudless_doc(p, granule.s2cloudless_doc)
            if granule.tesp_doc:
                _take_software_versions(p, granule.tesp_doc)

            _unpack_products(p, included_products, granule_group)

            if include_oa:
                with sub_product("oa", p):
                    with do("Starting OA", heading=True):
                        resolution_groups = {
                            tuple(granule_group[k].attrs["resolution"]): granule_group[
                                k
                            ]
                            for k in granule_group.keys()
                            if k.startswith("RES-GROUP-")
                        }

                        # Use the highest resolution as the ground sample distance.
                        if "eo:gsd" in p.properties:
                            del p.properties["eo:gsd"]
                        p.properties["eo:gsd"] = min(min(resolution_groups.keys()))

                        _unpack_observation_attributes(
                            p,
                            get_oa_resolution_group(
                                resolution_groups, p.platform, oa_resolution
                            ),
                        )

                    infer_datetime_range = p.platform.startswith("landsat")

                    with do("Contiguity", timedelta=infer_datetime_range):
                        # For landsat, we want the "common" band resolution, not panchromatic. Pick lower res.
                        if contiguity_resolution is not None:
                            contiguity_res = contiguity_resolution
                        elif p.platform.startswith("landsat"):
                            contiguity_res = max(resolution_groups.keys())
                        elif p.platform.startswith("sentinel"):
                            contiguity_res = (10.0, 10.0)

                        if contiguity_res not in resolution_groups:
                            raise ValueError(
                                f"No resolution group {contiguity_res} found in {granule.name}."
                                f"Options: {list(resolution_groups.keys())}"
                            )
                        contiguity_res_grp = resolution_groups[contiguity_res]

                        timedelta_data = (
                            contiguity_res_grp["SATELLITE-SOLAR/TIME-DELTA"]
                            if infer_datetime_range
                            else None
                        )
                        _create_contiguity(
                            p,
                            included_products,
                            resolution_yx=tuple(contiguity_res_grp.attrs["resolution"]),
                            timedelta_data=timedelta_data,
                        )

                    if granule.fmask_image:
                        with do(f"Writing fmask from {granule.fmask_image} "):
                            p.write_measurement(
                                "oa:fmask",
                                granule.fmask_image,
                                expand_valid_data=False,
                                overview_resampling=Resampling.mode,
                                # Because of our strange sub-products and filename standards, we want the
                                # 'oa_' prefix to be included in the recorded band metadata,
                                # but not in its filename.
                                # So we manually calculate a filename without the extra prefix.
                                path=p.names.measurement_filename("fmask"),
                            )

                    if granule.s2cloudless_prob:
                        with do(
                            f"Writing s2cloudless probability from {granule.s2cloudless_prob} "
                        ):
                            p.write_measurement(
                                "oa:s2cloudless_prob",
                                granule.s2cloudless_prob,
                                expand_valid_data=False,
                                overview_resampling=Resampling.bilinear,
                                path=p.names.measurement_filename("s2cloudless-prob"),
                            )

                    if granule.s2cloudless_mask:
                        with do(
                            f"Writing s2cloudless mask from {granule.s2cloudless_mask} "
                        ):
                            p.write_measurement(
                                "oa:s2cloudless_mask",
                                granule.s2cloudless_mask,
                                expand_valid_data=False,
                                overview_resampling=Resampling.mode,
                                path=p.names.measurement_filename("s2cloudless-mask"),
                            )

            with do("Finishing package"):
                return p.done()


def _read_gqa_doc(p: DatasetAssembler, doc: Dict):
    _take_software_versions(p, doc)
    p.extend_user_metadata("gqa", doc)

    # TODO: more of the GQA fields?
    for k, v in flatten_dict(doc["residual"], separator="_"):
        p.properties[f"gqa:{k}"] = v


def _read_fmask_doc(p: DatasetAssembler, doc: Dict):
    for name, value in doc["percent_class_distribution"].items():
        # From Josh: fmask cloud cover trumps the L1 cloud cover.
        if name == "cloud" and not isnan(value):
            if "eo:cloud_cover" in p.properties:
                del p.properties["eo:cloud_cover"]
            p.properties["eo:cloud_cover"] = value

        p.properties[f"fmask:{name}"] = value

    _take_software_versions(p, doc)
    p.extend_user_metadata("fmask", doc)


def _read_s2cloudless_doc(p: DatasetAssembler, doc: Dict):
    for name, value in doc["percent_class_distribution"].items():
        p.properties[f"s2cloudless:{name}"] = value

    _take_software_versions(p, doc)
    p.extend_user_metadata("s2cloudless", doc)


def _take_software_versions(p: DatasetAssembler, doc: Dict):
    versions = doc.pop("software_versions", {})

    for name, o in versions.items():
        p.note_software_version(name, o.get("repo_url"), o.get("version"))


def find_a_granule_name(wagl_hdf5: Path) -> str:
    """
    Try to extract granule name from wagl filename,

    >>> find_a_granule_name(Path('LT50910841993188ASA00.wagl.h5'))
    'LT50910841993188ASA00'
    >>> find_a_granule_name(Path('S2A_OPER_MSI_L1C_TL_EPAE_20201031T022859_A027984_T53JQJ_N02.09.wagl.h5'))
    'S2A_OPER_MSI_L1C_TL_EPAE_20201031T022859_A027984_T53JQJ_N02.09'
    >>> find_a_granule_name(Path('my-test-granule.h5'))
    Traceback (most recent call last):
    ...
    ValueError: Does not appear to be a wagl output filename? 'my-test-granule.h5'.
    """
    if not wagl_hdf5.name.endswith(".wagl.h5"):
        raise ValueError(
            f"Does not appear to be a wagl output filename? {wagl_hdf5.name!r}."
        )

    return wagl_hdf5.name[: -len(".wagl.h5")]


def _read_wagl_metadata(granule_group: h5py.Group):
    try:
        wagl_path, *ancil_paths = (
            pth for pth in _find_h5_paths(granule_group, "SCALAR") if "METADATA" in pth
        )
    except ValueError:
        raise ValueError("No nbar metadata found in granule")

    [wagl_doc] = loads_yaml(granule_group[wagl_path][()])

    for i, path in enumerate(ancil_paths, start=2):
        wagl_doc.setdefault(f"wagl_{i}", {}).update(
            list(loads_yaml(granule_group[path][()]))[0]["ancillary"]
        )
    return wagl_doc


def _apply_wagl_metadata(p: DatasetAssembler, wagl_doc: Dict):
    source = wagl_doc["source_datasets"]
    p.datetime = source["acquisition_datetime"]
    p.platform = source["platform_id"]
    p.instrument = source["sensor_id"]

    try:
        p.processed = get_path(wagl_doc, ("system_information", "time_processed"))
    except PathAccessError:
        raise RuntimeError("WAGL dataset contains no processed time.")

    _take_software_versions(p, wagl_doc)
    p.extend_user_metadata("wagl", wagl_doc)


def _determine_maturity(acq_date: datetime, processed: datetime, wagl_doc: Dict):
    """
    Determine maturity field of a dataset.

    Based on the fallback logic in nbar pages of CMI, eg: https://cmi.ga.gov.au/ga_ls5t_nbart_3
    """

    ancillary_tiers = {
        key.lower(): o["tier"]
        for key, o in wagl_doc["ancillary"].items()
        if "tier" in o
    }

    if "water_vapour" not in ancillary_tiers:
        # Perhaps this should be a warning, but I'm being strict until told otherwise.
        # (a warning is easy to ignore)
        raise ValueError(
            f"No water vapour ancillary tier. Got {list(ancillary_tiers.keys())!r}"
        )

    water_vapour_is_definitive = ancillary_tiers["water_vapour"].lower() == "definitive"

    if (processed - acq_date) < timedelta(hours=48):
        return "nrt"

    if not water_vapour_is_definitive:
        return "interim"

    # For accurate BRDF, both Aqua and Terra need to be operating.
    # Aqua launched May 2002, and we add a ~2 month buffer of operation.
    if acq_date < default_utc(datetime(2002, 7, 1)):
        return "final"

    if "brdf" not in ancillary_tiers:
        # Perhaps this should be a warning, but I'm being strict until told otherwise.
        # (a warning is easy to ignore)
        raise ValueError(
            f"No brdf tier available. Got {list(ancillary_tiers.keys())!r}"
        )
    brdf_tier = ancillary_tiers["brdf"].lower()

    if "definitive" in brdf_tier:
        return "final"
    elif "fallback" in brdf_tier:
        return "interim"
    else:
        # This value should not occur for production data, only for experiments
        return "user"
