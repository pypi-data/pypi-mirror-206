import os, glob, time
import logging
import argparse
from collections import OrderedDict
import numpy as np
import torch
import options.opt as option
import utils.util as util
from model_pipeline import ModelPipeline
from data import create_dataset, create_dataloader



def main(): 

    ## read option file
    parser = argparse.ArgumentParser()
    parser.add_argument('-opt', type=str, required=True, help='Path to options JSON file.')
    opt = option.parse(parser.parse_args().opt, is_train=False)
    opt = util.dict_to_nonedict(opt)
    
    ## set up logger
    util.setup_logger(None, opt['output']['log'], 'test.log', level=logging.INFO, screen=True)
    logger = logging.getLogger('base')
    logger.info(util.dict2str(opt))
    torch.backends.cudnn.benchmark = True
    
    ## define data loader 
    dataset_opt = opt['dataset']
    test_set = create_dataset(dataset_opt) # original input option
    test_loader = create_dataloader(test_set, dataset_opt) 
    logger.info('Number of test volumes in [{:s}]: {:d}'.format(dataset_opt['source'], len(test_set)))

    ## create a pipeline 
    pipeline = ModelPipeline(opt)
        
    ## loop over the data loader and run the pipeline on each batch 
    for i, data in enumerate(test_loader):
        print('Processing case: {}'.format(i))
        output = pipeline.run_pipeline(data)

        if opt['gpu_ids']: 
            torch.cuda.synchronize()
    


if __name__ == '__main__':
    main()

