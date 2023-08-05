from typing import Optional
import numpy as np
import pandas as pd
import torch
import tqdm
import ubelt as ub
import logging
import yaml
from scipy import ndimage
from skimage import morphology as sm
from skimage.measure import regionprops
from skimage.measure._regionprops import _props_to_dict
from skimage.segmentation import clear_border
from pathlib import Path
from functools import lru_cache

from emcaps.utils.patch_utils import measure_outer_disk_radius
from emcaps import utils


# Set up logging
logger = logging.getLogger('emcaps-iu')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(f'{utils.TMPPATH}/emcaps-iu.log')
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f'Running on {DEVICE}')
DTYPE = torch.float16 if 'cuda' in str(DEVICE) else torch.float32


# From https://github.com/napari/napari/blob/5cfcc38c0a313f42cc8b0f82ac3db945874ae362/examples/annotate_segmentation_with_text.py#L75
def calculate_circularity(perimeter, area):
    """Calculate the circularity of the region

    Parameters
    ----------
    perimeter : float
        the perimeter of the region
    area : float
        the area of the region

    Returns
    -------
    circularity : float
        The circularity of the region as defined by 4*pi*area / perimeter^2
    """
    circularity = 4 * np.pi * area / (perimeter ** 2)

    return circularity


# From https://github.com/napari/napari/blob/5cfcc38c0a313f42cc8b0f82ac3db945874ae362/examples/annotate_segmentation_with_text.py#L46
def make_bbox(bbox_extents):
    """Get the coordinates of the corners of a
    bounding box from the extents

    Parameters
    ----------
    bbox_extents : list (4xN)
        List of the extents of the bounding boxes for each of the N regions.
        Should be ordered: [min_row, min_column, max_row, max_column]

    Returns
    -------
    bbox_rect : np.ndarray
        The corners of the bounding box. Can be input directly into a
        napari Shapes layer.
    """
    minr = bbox_extents[0]
    minc = bbox_extents[1]
    maxr = bbox_extents[2]
    maxc = bbox_extents[3]

    bbox_rect = np.array(
        [[minr, minc], [maxr, minc], [maxr, maxc], [minr, maxc]]
    )
    bbox_rect = np.moveaxis(bbox_rect, 2, 0)

    return bbox_rect


class_name_colors = utils.class_info['class_name_colors']
class_ids_bgi = utils.class_info['class_ids_bgi']

# Convert to float RGBA (all elements in range [0, 1]) because both napari and skimage expect this range
class_colors = {
    class_ids_bgi[k]: np.array(v, dtype=np.float32) / 255.
    for k, v in class_name_colors.items()
}

color_cycle = []
for i in sorted(class_colors.keys()):
    col = class_colors[i]
    color_cycle.append(col)

# For skimage rendering the background gets special treatment and needs to be removed from the color cycle.
skimage_color_cycle = color_cycle.copy()[1:]


# Load model registry
repo_root = Path(__file__).parents[2]
model_registry_path = repo_root / 'emcaps/model_registry.yaml'
with open(model_registry_path) as f:
    model_registry = yaml.load(f, Loader=yaml.FullLoader)
segmenter_urls = model_registry['segmenter_urls']
classifier_urls = model_registry['classifier_urls']

model_urls = {**segmenter_urls, **classifier_urls}


class Randomizer(torch.nn.Module):
    """Test model for producing correctly shaped random outputs in range [0, 1]"""
    def forward(self, x):
        return torch.rand(x.shape[0], 2, *x.shape[2:])


@lru_cache(maxsize=32)
def get_model(path_or_name: str) -> Optional[torch.jit.ScriptModule]:
    if path_or_name in model_urls.keys():
        url = model_urls[path_or_name]
        if url == 'NA':  # not available
            # logger.info(f'Model {url} is not available.')
            return None
        local_path = ub.grabdata(url, appname='emcaps')
    else:
        if (p := Path(path_or_name).expanduser()).is_file():
            local_path = p
        else:
            raise ValueError(f'Model {path_or_name} not found. Valid choices are existing file paths or the following short names:\n{list(model_urls.keys())}')
    model = load_torchscript_model(local_path)
    return model


def load_torchscript_model(path: str) -> torch.jit.ScriptModule:
    model = torch.jit.load(path, map_location=DEVICE).eval().to(DTYPE)
    # model = torch.jit.optimize_for_inference(model)  # Works sometimes, but not in all environments
    return model


def normalize(image: np.ndarray) -> np.ndarray:
    normalized = (image.astype(np.float32) - 128.) / 128.
    assert normalized.min() >= -1.
    assert normalized.max() <= 1.
    return normalized


def segment(image: np.ndarray, thresh: float, segmenter_variant: str) -> np.ndarray:
    # return image > 0.9
    seg_model = get_model(segmenter_variant)
    img = torch.from_numpy(image)[None, None].to(device=DEVICE, dtype=DTYPE)
    with torch.inference_mode():
        out = seg_model(img)
        # pred = torch.argmax(out, dim=1)
        pred = out[0, 1] > thresh
        pred = pred.cpu().numpy().astype(np.int64)
    return pred


def calculate_padding(current_shape, target_shape):
    """Calculate optimal padding for np.pad() to do central padding to target shape.

    If necessary (odd shape difference), pad 1 pixel more before than after."""
    halfdiff = np.subtract(target_shape, current_shape) / 2  # Half shape difference (float)
    fd = np.floor(halfdiff).astype(int)
    cd = np.ceil(halfdiff).astype(int)
    padding = (
        (fd[0], cd[0]),
        (fd[1], cd[1])
    )
    return padding


def assign_class_names(pred_ids):
    pred_class_names = [utils.CLASS_NAMES[pred] for pred in pred_ids]
    return pred_class_names


def check_image(img, normalized=False, shape=None):
    _min = 0
    _max = 255
    if normalized:
        _min = normalize(np.array(_min))
        _max = normalize(np.array(_max))
    if img.min() < _min or img.max() > _max:
        raise ImageError(f'{img.min()=}, {img.max()=} not within expected range [{_min}, {_max}]')
    if shape is not None and not np.all(np.array(img.shape) == np.array(shape)):
        raise ImageError(f'{img.shape=}, but expected {shape}')


def classify_patch(patch, classifier_variant, allowed_classes=utils.CLASS_GROUPS['simple_hek']):

    inp = normalize(patch)
    check_image(inp, normalized=True)

    classifier_model = get_model(classifier_variant)

    allowed_class_ids = [utils.CLASS_IDS[cn] for cn in allowed_classes]

    inp = torch.from_numpy(inp)[None, None].to(device=DEVICE, dtype=DTYPE)
    with torch.inference_mode():
        out = classifier_model(inp)
        out = torch.softmax(out, 1)
        # for c in range(out.shape[1]):
        #     if not c in allowed_class_ids:
        #         out[:, c] = 0.
        excluded_class_ids = set(range(out.shape[1])) - set(allowed_class_ids)
        for c in excluded_class_ids:
            out[:, c] = 0.
        pred = torch.argmax(out, dim=1)[0].item()
        # pred -= 2 #p2
    return pred


def compute_rprops(
    image,
    lab,
    classifier_variant,
    minsize=60,
    maxsize=None,
    noborder=False,
    min_circularity=0.8,
    inplace_relabel=False,
    allowed_classes=utils.CLASS_GROUPS['simple_hek'],
    return_relabeled_seg=False,
    dilate_masks_by=5,
    ec_region_radius=24,

):
    # Code mainly redundant with / copied from patchifyseg. TODO: Refactor into shared function

    # Add 1 to high region coordinate in order to arrive at an odd number of pixels in each dimension
    EC_REGION_ODD_PLUS1 = 1

    DILATE_MASKS_BY = dilate_masks_by
    EC_REGION_RADIUS = ec_region_radius

    PATCH_WIDTH = EC_REGION_RADIUS * 2 + EC_REGION_ODD_PLUS1
    PATCH_SHAPE = (PATCH_WIDTH, PATCH_WIDTH)
    EC_MAX_AREA = (2 * EC_REGION_RADIUS)**2 if maxsize is None else maxsize
    EC_MIN_AREA = minsize
    MIN_CIRCULARITY = min_circularity

    raw = image

    check_image(raw, normalized=False)

    # remove artifacts connected to image border
    cleaned_lab = lab.copy()  # Can be modified without changing lab inplace
    if noborder:
        cleaned_lab = clear_border(cleaned_lab)
    cleaned_lab = ndimage.binary_fill_holes(cleaned_lab)
    cleaned_lab = sm.remove_small_objects(cleaned_lab, minsize)
    # cleaned_lab = sm.binary_erosion(cleaned_lab, footprint=sm.disk(3))  # Uncomment to erode before cc labeling

    # label image regions
    cc, n_comps = ndimage.label(cleaned_lab)

    rprops = regionprops(cc, raw)

    # epropdict = {k: np.full((len(rprops),), np.nan) for k in extra_prop_names}

    epropdict = {
        'class_id': np.empty((len(rprops),), dtype=np.uint8),
        'class_name': ['?'] * len(rprops),
        'circularity': np.empty((len(rprops),), dtype=np.float32),
        'radius2': np.empty((len(rprops),), dtype=np.float32),
        'is_invalid': np.empty((len(rprops),), dtype=bool),
    }

    if return_relabeled_seg:
        relabeled = lab.astype(np.uint8)

    for i, rp in enumerate(tqdm.tqdm(rprops, position=1, leave=True, desc='Analyzing regions', dynamic_ncols=True)):
        is_invalid = False
        centroid = np.round(rp.centroid).astype(np.int64)  # Note: This centroid is in the global coordinate frame
        if rp.area < EC_MIN_AREA or rp.area > EC_MAX_AREA:
            logger.info(f'Skipping: area size {rp.area} not within [{EC_MIN_AREA}, {EC_MAX_AREA}]')
            is_invalid = True
            continue  # Too small or too big (-> background component?) to be a normal particle
        circularity = np.nan
        if MIN_CIRCULARITY > 0:
            circularity = calculate_circularity(rp.perimeter, rp.area)
            if circularity < MIN_CIRCULARITY:
                logger.info(f'Skipping: circularity {circularity} below {MIN_CIRCULARITY}')
                is_invalid = True
                continue  # Not circular enough (probably a false merger)
            circularity = np.round(circularity, 2)  # Round for more readable logging

        lo = centroid - EC_REGION_RADIUS
        hi = centroid + EC_REGION_RADIUS + EC_REGION_ODD_PLUS1
        if np.any(lo < 0) or np.any(hi > raw.shape):
            logger.info(f'Skipping: region touches border')
            is_invalid = True
            continue  # Too close to image border

        xslice = slice(lo[0], hi[0])
        yslice = slice(lo[1], hi[1])

        raw_patch = raw[xslice, yslice]
        # mask_patch = mask[xslice, yslice]
        # For some reason mask[xslice, yslice] does not always contain nonzero values, but cc at the same slice does.
        # So we rebuild the mask at the region slice by comparing cc to 0
        mask_patch = cc[xslice, yslice] > 0


        # Eliminate coinciding masks from other particles that can overlap with this region (this can happen because we slice the mask_patch from the global mask)
        _mask_patch_cc, _ = ndimage.label(mask_patch)
        # Assuming convex particles, the center pixel is always on the actual mask region of interest.
        _local_center = np.round(np.array(mask_patch.shape) / 2).astype(np.int64)
        _mask_patch_centroid_label = _mask_patch_cc[tuple(_local_center)]
        # All mask_patch pixels that don't share the same cc label as the centroid pixel are set to 0
        mask_patch[_mask_patch_cc != _mask_patch_centroid_label] = 0

        if mask_patch.sum() == 0:
            # No positive pixel in mask -> skip this one
            logger.info(f'Skipping: no particle mask in region')
            # TODO: Why does this happen although we're iterating over regionprops from mask?
            # (Only happens if using `mask_patch = mask[xslice, yslice]`. Workaround: `Use mask_patch = cc[xslice, yslice] > 0`)
            is_invalid = True
            continue

        area = int(np.sum(mask_patch))
        radius2 = np.round(measure_outer_disk_radius(mask_patch, discrete=False), 1)

        # Enlarge masks because we don't want to risk losing perimeter regions
        if DILATE_MASKS_BY > 0:
            disk = sm.disk(DILATE_MASKS_BY)
            # mask_patch = ndimage.binary_dilation(mask_patch, iterations=DILATE_MASKS_BY)
            mask_patch = sm.binary_dilation(mask_patch, footprint=disk)

        # Measure again after mask dilation
        area_dilated = int(np.sum(mask_patch))
        radius2_dilated = np.round(measure_outer_disk_radius(mask_patch, discrete=False), 1)

        # Raw patch with background erased via mask
        nobg_patch = raw_patch.copy()
        nobg_patch[mask_patch == 0] = 0

        check_image(nobg_patch, normalized=False, shape=PATCH_SHAPE)

        class_id = classify_patch(patch=nobg_patch, classifier_variant=classifier_variant, allowed_classes=allowed_classes)
        class_name = utils.CLASS_NAMES[class_id]

        if not is_invalid:
            if return_relabeled_seg:
                relabeled[tuple(rp.coords.T)] = class_id
            if inplace_relabel:
                # This feels (morally) wrong but it seems to work.
                # Overwrite lab argument from caller by writing back into original memory
                lab[tuple(rp.coords.T)] = class_id

        # # Attribute assignments don't stick for _props_to_dict() for some reason
        # rp.class_id = class_id
        # rp.class_name = class_name
        # rp.circularity = circularity
        # rp.radius2 = radius2

        epropdict['class_id'][i] = class_id
        epropdict['class_name'][i] = class_name
        epropdict['circularity'][i] = circularity
        epropdict['radius2'][i] = radius2
        epropdict['is_invalid'][i] = is_invalid

        # iio.imwrite('/tmp/nobg-{i:03d}.png', nobg_patch)

    # Can only assign builtin props here
    propdict = _props_to_dict(
        rprops, properties=['label', 'bbox', 'perimeter', 'area', 'solidity', 'centroid']
    ) if len(rprops) > 0 else {}

    propdict.update(epropdict)

    is_invalid = propdict['is_invalid']
    num_invalid = int(np.sum(is_invalid))
    logger.info(f'Pruning {num_invalid} regions due to filter criteria...')
    for k in propdict.keys():
        propdict[k] = np.delete(propdict[k], is_invalid)

    if return_relabeled_seg:
        return propdict, relabeled

    return propdict


def save_properties_to_xlsx(properties: dict, xlsx_out_path: Path) -> None:
    if not properties or properties['class_id'].size == 0:
        logger.debug('properties empty -> not saving .xlsx file')
        return
    xlsx_out_path = xlsx_out_path.expanduser()
    # Create a dataframe from properties for saving to an .xlsx file
    propframe = pd.DataFrame(properties)
    propframe = propframe.round(2)  # Round every float entry to 2 decimal places
    propframe.rename(columns={'label': 'region_id'}, inplace=True)  # Rename misleading column for conn. comp. id
    # Select and reorder columns of interest
    selected_columns = ['region_id'] +\
                       ['class_id', 'class_name'] +\
                       ['area', 'radius2'] +\
                       [f'centroid-{i}' for i in range(2)] +\
                       [f'bbox-{i}' for i in range(4)]
    propframe = propframe[selected_columns]
    logger.info(f'Writing output to {xlsx_out_path}')
    # Save to spreadsheet
    propframe.to_excel(xlsx_out_path, sheet_name='emcaps-regions', index=False)


def compute_majority_class_name(class_preds):
    majority_class = np.argmax(np.bincount(class_preds))
    majority_class_name = assign_class_names([majority_class])[0]
    return majority_class_name


class ImageError(Exception):
    pass
