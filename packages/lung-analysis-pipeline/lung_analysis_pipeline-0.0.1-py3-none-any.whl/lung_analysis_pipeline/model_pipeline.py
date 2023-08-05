from lung_analysis_pipeline.Normalization_Pipeline.codes.models import create_model as create_normalization_model
from lung_analysis_pipeline.NoduleSeg_MedicalNet.build_unet_model import create_seg_model 
import lung_analysis_pipeline.utils.util as util
import numpy as np 
import os 
import torch

def print_model_name(model_name): 
    print('running model: ', model_name)
def detection_model(input_data): 
    print('detection')
    return input_data
def feature_extraction(input_data):
    print('feature extractor')
    return input_data


class ModelPipeline: 
    def __init__(self, opt):
        # self.models = models 
        self.opt = opt 
        self._check_order(opt)
        order = self.opt['order']
        if 'normalization' in order: 
            self.norm_model = create_normalization_model(opt)
        if 'detection' in order: 
            self.detect_model = util.PythonFunctionWrapper(detection_model)
        if 'segmentation' in order: 
            self.seg_model = create_seg_model(in_nc=1, out_nc=1, nf=64)
        if 'feature_extraction' in order:
            self.feature_extractions = [util.PythonFunctionWrapper(feature_extraction)]

    def run_pipeline(self, input_data): 

        output = input_data 
        # save_vol(opt, spacings, results_dir, patient_id, volume)
        results_dir = self.opt['output']['output_location']
        
        if hasattr(self, 'norm_model'):
            input_data = self.norm_model.run_test(input_data)

            # save norm output 
            need_HR = False if self.opt['dataset']['dataroot_HR'] is None else True
            has_mask = False if self.opt['dataset']['maskroot_HR'] is None else True

            visuals = self.norm_model.get_current_visuals(input_data, maskOn=has_mask, need_HR=need_HR)
            # save volume data
            norm_results_dir = os.path.join(results_dir, 'normalization')
            util.mkdir(norm_results_dir)

            sr_vol = util.tensor2img(visuals['SR'], out_type=np.uint16)
            util.save_vol(self.opt, [], norm_results_dir, input_data['uid'][0], sr_vol)
        
        if hasattr(self, 'detect_model'):
            detect_output = self.detect_model.run_test(input_data)
        
        if hasattr(self, 'seg_model'): 
            if self.opt['segmentation']['use_decetion_bbox']: 
                seg_output = self.seg_model.run_test(detect_output) 
            else: 
                seg_output = self.seg_model.run_test(input_data) 

                seg_ressult_dir = os.path.join(results_dir, 'segmentation')
                util.mkdir(seg_ressult_dir)

                seg_output = util.tensor2mask(seg_output['seg_mask'][0][0], out_type=np.uint16)
                util.save_vol(self.opt, [], seg_ressult_dir, input_data['uid'][0], seg_output)

        if hasattr(self, 'feature_extractions'): 
            for extractor in self.feature_extractions: 
                ## extract feature 
                if self.opt['feature_extraction']['use_segmentation']: # use segmentation output 
                    features = extractor.run_test(seg_output)
                else: # use specified masks and input data
                    features = extractor.run_test(input_data)
                ## save features 
        if self.opt['gpu_ids']: 
            torch.cuda.synchronize()

    """
    Check if specified operations are allowed. 
    """
    def _check_order(self, opt): 
        order = opt['order']
        for i, ops in enumerate(order): 
            if not opt[ops]:
                raise ValueError('Please specify {} operation.'.format(ops))
            if ops == 'normalization': 
                if i != 0: 
                    raise ValueError('Normalization operation order not supported!')
            elif ops == 'segmentation': 
                # there has to exist detection before seg or use detection is set to false 
                if opt['segmentation']['use_decetion_bbox'] and not 'detection' in order[:i]: 
                    raise ValueError('Segmentation operation order not supported!')
            elif ops == 'feature_extraction': 
                if not 'segmentation' in order[:i] and not opt['dataset']['mask_location']:
                    raise ValueError('Segmentation operation order not supported! Need to specify masks or use segmentation.')
                opt['feature_extraction']['use_segmentation'] = True

