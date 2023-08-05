import logging
import lung_analysis_pipeline.utils.util as util
import lung_analysis_pipeline.options.opt as option
import argparse
import torch

def create_logger(opt): 
    ## set up logger
    util.setup_logger(None, opt['output']['log'], 'test.log', level=logging.INFO, screen=True)
    logger = logging.getLogger('base')
    logger.info(util.dict2str(opt))
    torch.backends.cudnn.benchmark = True
    return logger 

def create_option():
    ## read option file
    parser = argparse.ArgumentParser()
    parser.add_argument('-opt', type=str, required=True, help='Path to options JSON file.')
    opt = option.parse(parser.parse_args().opt, is_train=False)
    opt = util.dict_to_nonedict(opt)
    return opt 