"""
PyTorch Dataset classes for loading encapsulin segmentation and classification datasets.
"""

# TODO: Rename module

import logging
import hydra
import os
from functools import lru_cache
from pathlib import Path
from typing import Optional, Sequence, Tuple, Union, Callable

import imageio.v3 as iio
import numpy as np
import pandas as pd
import torch
from elektronn3.data import transforms
from skimage import morphology as sm
from torch.utils import data

from emcaps import utils

logger = logging.getLogger('emcaps-emcdata')


@lru_cache(maxsize=1024)
def mimread(*args, **kwargs):
    """Memoize imread to avoid disk I/O"""
    return iio.imread(*args, **kwargs)


# Credit: https://newbedev.com/how-can-i-create-a-circular-mask-for-a-numpy-array
def create_circular_mask(h, w, center=None, radius=None):
    if center is None:  # use the middle of the image
        center = (int(w / 2), int(h / 2))
    if radius is None:  # use the smallest distance between the center and image walls
        radius = min(center[0], center[1], w - center[0], h - center[1])
    yy, xx = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((xx - center[0])**2 + (yy - center[1])**2)
    mask = dist_from_center <= radius
    return mask


class EncPatchData(data.Dataset):
    """Image-level classification dataset loader for small patches, similar to MNIST"""
    def __init__(
            self,
            # data_root: str,
            descr_sheet: Tuple[Union[str, Path], str | int],
            train: bool = True,
            transform=transforms.Identity(),
            inp_dtype=np.float32,
            target_dtype=np.int64,
            dilate_masks_by: int = 0,
            erase_mask_bg: bool = False,
            erase_disk_mask_radius: int = 0,
            epoch_multiplier: int = 1,  # Pretend to have more data in one epoch
    ):
        super().__init__()
        # self.data_root = data_root
        self.train = train
        self.transform = transform
        self.inp_dtype = inp_dtype
        self.target_dtype = target_dtype
        self.dilate_masks_by = dilate_masks_by
        self.erase_mask_bg = erase_mask_bg
        self.erase_disk_mask_radius = erase_disk_mask_radius
        self.epoch_multiplier = epoch_multiplier

        sheet = pd.read_excel(descr_sheet[0], sheet_name=descr_sheet[1])
        self._sheet = sheet
        meta = sheet.copy()

        if self.train:
            logger.info('\nTraining data:')
            meta = meta.loc[meta.train == True]  # Explicit comparison due to possible integer types
        else:
            logger.info('\nValidation data:')
            meta = meta.loc[meta.validation == True]  # Explicit comparison due to possible integer types

        self.meta = meta

        # self.root_path = Path(data_root).expanduser()
        self.root_path = Path(descr_sheet[0]).parent

        self.inps = []
        self.targets = []

        for patch_meta in self.meta.itertuples():
            inp = mimread(self.root_path / 'raw' / patch_meta.patch_fname).copy()
            # cmax = mimread(self.root_path / 'cmax' / patch_meta.patch_fname.replace('raw', 'cmax')).copy()
            # cavg = mimread(self.root_path / 'cavg' / patch_meta.patch_fname.replace('raw', 'cavg')).copy()

            if self.erase_mask_bg:
                # Erase mask background from inputs
                mask = mimread(self.root_path / 'mask' / patch_meta.patch_fname.replace('raw', 'mask')).copy()
                if self.dilate_masks_by > 0:
                    disk = sm.disk(self.dilate_masks_by)
                    # mask_patch = ndimage.binary_dilation(mask_patch, iterations=DILATE_MASKS_BY)
                    mask = sm.binary_dilation(mask, footprint=disk)
                inp[mask == 0] = 0
            if self.erase_disk_mask_radius > 0:
                mask = create_circular_mask(*inp.shape, radius=self.erase_disk_mask_radius)
                inp[mask > 0] = 0

            # mask = mimread(self.root_path / 'mask' / patch_meta.patch_fname.replace('raw', 'mask'))
            # inp = mask * 255

            # inp = np.stack((inp, cmax, cavg), axis=0)

            target = utils.CLASS_IDS[patch_meta.enctype]
            self.inps.append(inp)
            self.targets.append(target)

        self.inps = np.stack(self.inps).astype(self.inp_dtype)
        self.targets = np.stack(self.targets).astype(self.target_dtype)

        for enctype in meta.enctype.unique():
            logger.info(f'{enctype}: {meta[meta.enctype == enctype].shape[0]}')

    def __getitem__(self, index):
        index %= len(self.meta)  # Wrap around to support epoch_multiplier
        inp = self.inps[index]
        target = self.targets[index]
        fname = self.meta.patch_fname.iloc[index]
        label_name = target
        fname = f'{fname} ({label_name})'
        if inp.ndim == 2:
            inp = inp[None]  # (C=1, H, W)
        # Pass None instead of target because scalar targets are not to be augmented.
        inp, _ = self.transform(inp, None)
        sample = {
            'inp': torch.as_tensor(inp),
            'target': torch.as_tensor(target),
            'fname': fname,
        }
        return sample

    def __len__(self):
        return len(self.meta) * self.epoch_multiplier


class EncSegData(data.Dataset):
    """Using a special TIF file directory structure for segmentation data loading.

    Version for segtrain.py and dataset v6+.
    For training on all conditions or a subset thereof."""
    def __init__(
            self,
            # data_root: str,
            label_names: Sequence[str],
            descr_sheet=(os.path.expanduser('/wholebrain/scratch/mdraw/tum/Single-table_database/Image_annotation_for_ML_single_table.xlsx'), 'all_metadata'),
            data_path: str = '/wholebrain/scratch/mdraw/tum/Single-table_database/isplitdata_v15',
            meta_filter = lambda x: x,
            tr_group: str = 'all',
            train: bool = True,
            transform: transforms.Transform = transforms.Identity(),
            offset: Optional[Sequence[int]] = (0, 0),
            inp_dtype=np.float32,
            target_dtype=np.int64,
            invert_labels=False,  # Fixes inverted TIF loading
            enable_inputmask: bool = False,
            enable_binary_seg: bool = False,
            ignore_far_background_distance: int = 0,
            enable_partial_inversion_hack: bool = False,
            dilate_targets_by: int = 0,
            epoch_multiplier=1,  # Pretend to have more data in one epoch
    ):
        super().__init__()
        # self.data_root = data_root
        self.label_names = label_names
        self.meta_filter = meta_filter
        self.tr_group = tr_group
        self.train = train
        self.transform = transform
        self.offset = offset
        self.inp_dtype = inp_dtype
        self.target_dtype = target_dtype
        self.invert_labels = invert_labels
        self.enable_inputmask = enable_inputmask
        self.ignore_far_background_distance = ignore_far_background_distance
        self.epoch_multiplier = epoch_multiplier
        self.enable_binary_seg = enable_binary_seg
        self.enable_partial_inversion_hack = enable_partial_inversion_hack
        self.dilate_targets_by = dilate_targets_by

        if self.ignore_far_background_distance:
            self.ifbd_disk = sm.disk(self.ignore_far_background_distance)
        if self.dilate_targets_by > 0:
            self.td_disk = sm.disk(self.dilate_targets_by)

        sheet = pd.read_excel(descr_sheet[0], sheet_name=descr_sheet[1])
        self.sheet = sheet
        meta = sheet.copy()
        meta = meta.rename(columns={'Image ID': 'num'})
        meta = meta.rename(columns={'Short Experimental Condition': 'scond'})
        meta = meta.convert_dtypes()

        meta = self.meta_filter(meta)

        # Only select images that are marked in the selected data group
        meta = meta.loc[meta[tr_group] == 1]


        # self.root_path = Path(descr_sheet[0]).parent / data_path
        self.root_path = Path(data_path).expanduser()
        logger.info(f'Getting data from {self.root_path}')

        # Not all images are always available
        self.available_img_nums = [
            num for num in meta.num.to_list()
            if (self.root_path / str(num)).is_dir()
        ]
        meta = meta.loc[meta.num.isin(self.available_img_nums)]

        self.meta = meta

        conditions = self.meta['scond'].unique()
        for condition in conditions:
            _nums = meta.loc[meta['scond'] == condition]['num'].to_list()
            logger.info(f'{condition}:\t({len(_nums)} images):\n {_nums}')

    def __getitem__(self, index):
        index %= len(self.meta)  # Wrap around to support epoch_multiplier
        # subdir_path = self.subdir_paths[index]
        mrow = self.meta.iloc[index]
        img_num = mrow['num']
        subdir_path = self.root_path / f'{img_num}'

        if self.train:
            inp_path = subdir_path / f'{img_num}_trn.png'
        else:
            inp_path = subdir_path / f'{img_num}_val.png'

        inp = mimread(inp_path).astype(self.inp_dtype)
        if inp.ndim == 2:  # (H, W)
            inp = inp[None]  # (C=1, H, W)

        labels = []
        for label_name in self.label_names:
            if self.train:
                label_path = subdir_path / f'{img_num}_trn_{label_name}.png'
            else:
                label_path = subdir_path / f'{img_num}_val_{label_name}.png'
            if label_path.exists():
                label = mimread(label_path).astype(np.int64)
                if self.invert_labels:
                    label = (label == 0).astype(np.int64)
                if self.enable_partial_inversion_hack and int(img_num) < 55:  # TODO: Investigate why labels are inverted although images look fine
                    label = (label == 0).astype(np.int64)
            else:  # If label is missing, make it a full zero array
                label = np.zeros_like(inp[0], dtype=np.int64)
            labels.append(label)
        assert len(labels) > 0

        # Flat target filled with label indices
        target = np.zeros_like(labels[0], dtype=np.int64)
        # for c in range(len(self.label_names)):
        #     # Assign label index c to target at all locations where the c-th label is non-zero
        #     target[labels[c] != 0] = c

        target[labels[1] != 0] = 1

        if self.enable_binary_seg:  # Don't distinguish between foreground classes, just use one foreground class
            target[target > 0] = 1

        if self.enable_inputmask:  # Zero out input where target == 0 to make background invisible
            for c in range(inp.shape[0]):
                inp[c][target == 0] = 0

        if target.mean().item() > 0.4:
            print('Unusually high target mean in image number', img_num)

        if self.dilate_targets_by > 0:
            target = sm.binary_dilation(target, footprint=self.td_disk).astype(target.dtype)

        # Mark regions to be ignored
        if self.ignore_far_background_distance > 0 and mrow['scond'] == 'HEK-1xTmEnc-BC2-Tag':
            dilated_foreground = sm.binary_dilation(target, footprint=self.ifbd_disk)
            far_background = ~dilated_foreground
            target[far_background] = -1

        while True:  # Only makes sense if RandomCrop is used
            try:
                inp, target = self.transform(inp, target)
                break
            except transforms._DropSample:
                pass
        if np.any(self.offset):
            off = self.offset
            target = target[off[0]:-off[0], off[1]:-off[1]]
        sample = {
            'inp': torch.as_tensor(inp.astype(self.inp_dtype)),
            'target': torch.as_tensor(target.astype(self.target_dtype)),
            'fname': f'{subdir_path.name} ({mrow["scond"]})',
        }
        return sample

    def __len__(self):
        return len(self.meta) * self.epoch_multiplier
