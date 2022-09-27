import nibabel as nib
import numpy as np 


def random_crop_3d(img_arr_list, patch_size):
    pass
    
def center_crop():
    pass

def resample():
    pass

def normalize(arr, method='01'):
    return (arr - np.mean(arr)) / np.std(arr)