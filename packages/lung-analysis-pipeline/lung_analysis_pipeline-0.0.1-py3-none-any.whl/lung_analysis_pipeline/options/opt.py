import os
import os.path as osp
import logging
from collections import OrderedDict
import json
import lung_analysis_pipeline.utils.util as util

def parse(opt_path, is_train=False):
    # remove comments starting with '//'
    json_str = ''
    with open(opt_path, 'r') as f:
        for line in f:
            line = line.split('//')[0] + '\n'
            json_str += line
    opt = json.loads(json_str, object_pairs_hook=OrderedDict)

    results_root = opt['output']['output_location']
    opt['output']['log'] = results_root
    util.mkdir(results_root) 

    gpu_list = ','.join(str(x) for x in opt['gpu_ids']) if opt['gpu_ids'] else ""
    os.environ['CUDA_VISIBLE_DEVICES'] = gpu_list
    print('export CUDA_VISIBLE_DEVICES=' + gpu_list)

    return opt

