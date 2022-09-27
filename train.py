import os, time
from config.global_train_config import config
import torch
import numpy as np
import random

## For reproducible results    
def seed_all(s):
    np.random.seed(s)
    random.seed(s)
    os.environ['PYTHONHASHSEED'] = str(s) 
    torch.manual_seed(s)
    print(f'Seeds set to {s}!')

if not config.using_HPC:
    os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    os.environ["CUDA_VISIBLE_DEVICES"] = f"{config.gpu}"

if __name__ == "__main__":

    seed_all(42) #Set random seeds for reproducibility

    if config.project == 'PROJECTNAME':
        from src.model.archs.PROJECTNAME import MODELCLASS
        model = MODELCLASS(config)
    else:
        raise NotImplementedError

    if config.continue_epoch != '-1':
        model.load_epoch(config.continue_epoch)

    startTime = time.time()
    model.train()
    print(f'Training {config.project} model took {time.time() - startTime} seconds')

    print('Optimization done.')
