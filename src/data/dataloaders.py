import torch.utils.data as data
import pickle as pkl
import os
import torch
import random
import numpy as np
from glob import glob
from src.model.loss import global_mutual_information
import src.model.functions as smfunction
import src.data.preprocess as pre

torch.set_default_tensor_type('torch.FloatTensor')


class INSERTTYPEData(data.Dataset):
    def __init__(self, config, phase):
        self.phase = phase
        assert phase in ['train', 'val', 'test'], "phase cannot recongnise..."
        self.config = config
        self.data_path = self.config.data_path
        self.data_pairs = self.__get_data_pairs__()

    def __getitem__(self, index):
        pass

    def __len__(self):
        pass

    def __get_data_pairs__(self):
        pass

    def __get_inter_pairs__(self, index):
        pass

    @staticmethod
    def rand_prob(p=0.5):
        assert 0<=p<=1, "p should be a number in [0, 1]"
        return random.random() < p

    def random_crop_aug(self, seg_arr):
        pass
        
        
        
