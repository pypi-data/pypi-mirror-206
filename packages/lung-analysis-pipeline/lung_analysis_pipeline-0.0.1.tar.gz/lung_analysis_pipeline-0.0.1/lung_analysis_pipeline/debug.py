import numpy as np
import torch.utils.data as data
import SimpleITK as sitk
import pydicom
import utils.util as util
import random
import os, glob
import torch
import nrrd 
from utils import patch as patch_util
import nibabel



data_path  = '/datasets/NLST_CT_annotations/10076_113873/2001-01-02/CT Chest at TLC Supine-1.2.840.113654.2.55.168169096365492133736408631125872558059'

img_dir_path = os.path.join(data_path, 'DICOM')
# LR: extract volume cube during training, else return volume during validation 
dcm_files = [os.path.join(img_dir_path, f) for f in os.listdir(img_dir_path) if f.endswith('.dcm')]
dcm_files.sort(key=lambda x: int(pydicom.dcmread(x).InstanceNumber))
slices = [pydicom.dcmread(f) for f in dcm_files]
vol_in = np.stack([slice.pixel_array for slice in slices], axis=0).astype(np.float16)
print('vol shape: {}'.format(vol_in.shape))

mask_dir_path = os.path.join(data_path, 'Contours', 'NIFTI')
nifti_files = [os.path.join(mask_dir_path, f) for f in os.listdir(mask_dir_path) if f.endswith('.nii.gz') and f.startswith('Lesion')]
for f in nifti_files: 
    mask = nibabel.load(f).get_fdata()  # (512, 512, D)
    print('before: {}'.format(mask.shape))
    mask = np.transpose(mask, (2, 1, 0)) # [W,H,D]==>[D,H,W]
    print('after: {}'.format(mask.shape))

#     seg_mask += mask 
# seg_mask[seg_mask > 1] = 1 