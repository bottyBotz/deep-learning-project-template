import nibabel as nib
import os
import numpy as np
# from scipy import ndimage
# import nibabel as nib
# import matplotlib.pyplot as plt
# import cv2


def save_img(tensor_arr, save_path, pixdim=[1.0, 1.0, 1.0]):
    save_folder = os.path.dirname(save_path)
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
        
    arr = np.squeeze(tensor_arr)
    assert len(arr.shape)==3, "not a 3 dimentional volume, need to check."

    nib_img = nib.Nifti1Image(arr, affine=np.eye(4))
    nib_img.header['pixdim'][1:4] = np.array(pixdim)
    nib.save(img=nib_img, filename=save_path)
    
    

save_root = 'WHERE TO SAVE THE IMAGES'
src_root = 'WHERE TO GET THE RAW IMAGES'

for k in ['moving_images', 'moving_labels', 'fixed_images', 'fixed_labels']:
    os.makedirs(os.path.join(save_root, k), exist_ok=True)

class DATAPREPROCESSED(object):
    def __init__(self, pid):
        pass



