import SimpleITK as sitk
import torch.utils.data as data
import lung_analysis_pipeline.utils.util as util
import random
import os, glob
import torch
import numpy as np 
import nrrd
import nibabel
import pydicom

class dcmDataset(data.Dataset):
    def __init__(self, opt): 
        super(dcmDataset, self).__init__()
        self.FILL_RATIO_THRESHOLD = 0.8
        self.opt = opt
        self.in_folder = opt['dataroot_LR']

        # 3d voxel size
        if self.opt['phase'] == 'train' or (self.opt['phase'] =='val' and self.opt['need_voxels']):
            self.ps = (opt['LR_slice_size'], opt['LR_size'], opt['LR_size'])
        self.paths, self.uids = util.get_dcm_paths(opt['dataroot_LR'])

        self.scale = opt['scale']
        self.ToTensor = util.ImgToTensor()

    def __len__(self): 
        return len(self.paths)
    
    def __getitem__(self, index):
        data_dir_path = os.path.join(self.paths[index], 'DICOM')
        mask_dir_path = os.path.join(self.paths[index], 'Contours', 'NIFTI')
        splits = os.path.normpath(data_dir_path).split(os.sep)
        input_info = {'patient_id': splits[3], 'time': splits[4], 'name': splits[5]}

        # LR: extract volume cube during training, else return volume during validation 
        dcm_files = [os.path.join(data_dir_path, f) for f in os.listdir(data_dir_path) if f.endswith('.dcm')]
        dcm_files.sort(key=lambda x: int(pydicom.dcmread(x).InstanceNumber))
        slices = [pydicom.dcmread(f) for f in dcm_files]
        vol_in = np.stack([slice.pixel_array for slice in slices], axis=0).astype(np.float16)

        # creates an extra dimension. e.g. 32x64x64 becomes 1x32x64x64
        vol_in = np.expand_dims(vol_in, axis=0)

        # convert to tensors and also within a certain range of values as defined in 'self.ToTensor()' class
        vol_in = self.ToTensor(vol_in, clip=True, raw_data_range=1500.)

        # load segmentation mask 
        nifti_files = [os.path.join(mask_dir_path, f) for f in os.listdir(mask_dir_path) if f.endswith('.nii.gz') and f.startswith('Lesion')]
        seg_mask = np.zeros_like(vol_in)
        for f in nifti_files: 
            mask = nibabel.load(f).get_fdata()  # (512, 512, D)
            mask = np.transpose(mask, (2, 1, 0)) # [W,H,D]==>[D,H,W]
            seg_mask += mask 
        seg_mask[seg_mask > 1] = 1 

        # generate a volume id 
        patient_id = slices[0].PatientID.replace("_", "-")
        timepoint = slices[0].StudyDate
        series_instance_uid = slices[0].SeriesInstanceUID
        modality = slices[0].Modality 
        volume_id = f"{patient_id}_{timepoint}_{series_instance_uid}_{modality}"

        out_dict = {'LR': vol_in, 'seg_mask': seg_mask, 'spacings': [], 'uid': volume_id, 'input_info': input_info}
        # out_dict = {'LR': vol_in, 'HR': vol_in, 'mask': vol_in, 'spacings': [], 'uid': self.uids[index], 'input_info': input_info}

        return out_dict
