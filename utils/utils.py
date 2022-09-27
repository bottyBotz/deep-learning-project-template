import numpy as np
import random
import torch
import os
import time

def seed_all(s, use_cuda=True):
    """
    Set the seed for multiple libraries to ensure reproducibility.
    
    This function sets the random seed for numpy, the built-in random module, 
    torch, and also sets the PYTHONHASHSEED environment variable. This is useful
    when one wants to ensure reproducible results across runs, especially in 
    machine learning experiments.

    Parameters:
    - s (int): The seed value.
    - use_cuda (bool): A flag to indicate if CUDA is being used. Default is True.

    Returns:
    None
    """
    
    # Set the seed for numpy's random number generator.
    np.random.seed(s)
    
    # Set the seed for Python's built-in random module.
    random.seed(s)
    
    # Set the PYTHONHASHSEED environment variable. This is used by Python to seed 
    # the hashes of strings and bytes.
    os.environ['PYTHONHASHSEED'] = str(s) 
    
    # Set the seed for PyTorch's random number generator.
    torch.manual_seed(s)
    
    # If using CUDA, set further seeds and deterministic mode.
    if use_cuda:
        torch.cuda.manual_seed_all(s)
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False
    
    # Print a confirmation message.
    print(f'Seeds set to {s}!')

    

def timing_decorator(func):
    """
    A decorator that prints the time a function takes to execute.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__} took {elapsed_time:.2f} seconds to run.")
        return result

    return wrapper

    
    