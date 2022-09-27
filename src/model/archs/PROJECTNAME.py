from src.model import loss
import src.model.functions as smfunctions
from src.model.archs.baseArch import BaseArch
from src.data import dataloaders
import torch, os
import torch.optim as optim
from torch.utils.data import DataLoader
import pickle as pkl
import numpy as np
from scipy import stats
import cv2, random


class PROJECTNAME(BaseArch):
    def __init__(self, config):
        super(PROJECTNAME, self).__init__(config) #https://www.pythonforbeginners.com/super/working-python-super-function
        self.config = config
        self.net = self.net_parsing()
        self.set_dataloader()
        self.best_metric = 0

    def net_parsing(self):
        model = self.config.model
        if model == 'MODELNAME':
            net = MODELNAME(self.config)
        else:
            raise NotImplementedError
        return net.cuda()

    # def set_dataloader(self):
    #     self.train_set = dataloaders.CBCTData(config=self.config, phase='train')
    #     self.train_loader = DataLoader(
    #         self.train_set, 
    #         batch_size=self.config.batch_size,  
    #         num_workers=4,
    #         shuffle=True, 
    #         drop_last=True)
    #     print('>>> Train set ready.')  
    #     self.val_set = dataloaders.DATATYPEData(config=self.config, phase='val')
    #     self.val_loader = DataLoader(self.val_set, batch_size=1, shuffle=False)
    #     print('>>> Validation set ready.')
    #     self.test_set = dataloaders.DATATYPEData(config=self.config, phase='test')
    #     self.test_loader = DataLoader(self.test_set, batch_size=1, shuffle=False)
    #     print('>>> Holdout set ready.')

    # def get_input(self, input_dict, aug=True):
    #     """Get input to the network

    #     Args:
    #         input_dict (ndarray): data and label tensors
    #         aug (bool, optional): Whether to perform data augmentation.

    #     Raises:
    #         NotImplementedError: If the input mode is not valid (defined in your config)

    #     Returns:
    #         tensor : Correct type of input tensor combining fixed and moving image and label tensors
    #     """      
    #     fx_img, mv_img = input_dict['fx_img'].cuda(), input_dict['mv_img'].cuda()  # [batch, 1, x, y, z]
    #     fx_seg, mv_seg = input_dict['fx_seg'].cuda(), input_dict['mv_seg'].cuda()  # label
        

    #     return fx_img, fx_seg, mv_img, mv_seg
    

    # def train(self):
    #     """
    #     Training and validation loop for the model. Writes to tensorboard and logs directory for the current folds training and validation. 
    #     Performs inference on the holdout set after training.
    #     """        
    #     self.save_configure()
    #     optimizer = optim.Adam(self.net.parameters(), lr=self.config.lr, weight_decay=1e-6)
    #     log_dir = f"./logs/{self.config.project}"
    #     log_save_path = os.path.join(log_dir, 'running_logs')
    #     os.makedirs(log_save_path, exist_ok=True)
    #     with open(os.path.join(log_save_path, f'{self.config.exp_name}_train_log_{self.config.cv}.txt'), 'w') as f:
    #         f.write(f"project,exp_name,fold,train_val_test,epoch,value,value_type\n")
    #         for self.epoch in range(1, self.config.num_epochs + 1):
    #             self.net.train()
    #             print('-' * 10, f'Train epoch_{self.epoch}', '-' * 10)
    #             for self.step, input_dict in enumerate(self.train_loader):
    #                 fx_img, fx_seg, mv_img, mv_seg = self.get_input(input_dict) 

    #                 optimizer.zero_grad() # clear gradients
    #                 pred_seg = self.net(torch.cat([fx_img, mv_img, mv_seg], dim=1)) # forward pass
    #                 global_loss = self.loss() # compute loss
    #                 global_loss.backward() # backward pass
    #                 optimizer.step() #Gradient Descent

    #             #Save the model at periodic frequencies
    #             if self.epoch % self.config.save_frequency == 0:
    #                 self.save()
    #             print('-' * 10, 'validation', '-' * 10) 
                
    #             #Run the validation step
    #             self.validation(f) 
    #     #Run Holdout Test Set for this fold.
    #     self.inference()

    # def loss(self):
    #     L_All = 0
    #     #TODO: Implement per your loss function.
    #     return L_All

    # @torch.no_grad() #No Gradient Computation for validation step
    # def validation(self, f = None):
    #     self.net.eval() # Set model to validation/evaluation Mode
    #     res = []
    #     #Iterate through the validation dataloader
    #     for idx, input_dict in enumerate(self.val_loader):
    #         fx_img, fx_seg, mv_img, mv_seg = self.get_input(input_dict, aug=False)
    #         for label_idx in range(fx_seg.shape[2]):
    #             pred_seg = self.net(torch.cat([fx_img, mv_img, mv_seg[:, :, label_idx, ...]], dim=1))
    #             binary_dice = loss.binary_dice(pred_seg, fx_seg[:, :, label_idx, ...])
    #             subject = input_dict['subject']
    #             self.writer.add_scalar(f"{self.config.project}/{self.config.exp_name}/binary_dice/validation/subject_{subject}/label_idx_{label_idx}", binary_dice, self.epoch)

    #             print(f'subject:{subject}', f'label_idx:{label_idx}', f'DICE:{binary_dice:.3f}')
    #             res.append(binary_dice)


    #     res = torch.tensor(res)
    #     mean, std = torch.mean(res), torch.std(res)

    #     f.write(f"{self.config.project},{self.config.exp_name},{self.config.cv},'val',{self.epoch},{mean},'dice_mean'\n") # Write Dice Mean for Epoch to Log File
    #     f.write(f"{self.config.project},{self.config.exp_name},{self.config.cv},'val',{self.epoch},{std},'dice_std'\n") # Write Dice Std for Epoch to Log File

    #     #Save the best model as it's performance on the validation set
    #     if mean > self.best_metric:
    #         self.best_metric = mean
    #         print('better model found.')
    #         self.save(type='best')
    #     print('Dice:', mean, std)

    # @torch.no_grad() #No Gradient Computation for inference step
    # def inference(self):
    #     self.net.eval() #set model to test/eval mode
    #     visualization_path = os.path.join(self.log_dir, f'{self.config.exp_name}-vis-{self.epoch}')
    #     os.makedirs(visualization_path, exist_ok=True)

    #     results = {
    #         'dice': [],
    #         'dice-wo-reg': [],
    #         }

    #     #Iterate through the test data loader
    #     for idx, input_dict in enumerate(self.test_loader):
    #         fx_img, fx_seg, mv_img, mv_seg = self.get_input(input_dict, aug=False)
    #         self.save_img(fx_img, os.path.join(visualization_path, f'{idx+1}-fx_img.nii'))
    #         self.save_img(mv_img, os.path.join(visualization_path, f'{idx+1}-mv_img.nii'))

    #         label_num = fx_seg.shape[2]
    #         for label_idx in range(fx_seg.shape[2]):
    #             pred_seg = self.net(torch.cat([fx_img, mv_img, mv_seg[:, :, label_idx, ...]], dim=1)) #Forward Pass

    #             aft_dice = loss.binary_dice(pred_seg, fx_seg[:, :, label_idx, ...]).cpu().numpy()
    #             bef_dice = loss.binary_dice(fx_seg[:, :, label_idx, ...], mv_seg[:, :, label_idx, ...]).cpu().numpy()

    #             subject = input_dict['subject']
    #             results['dice'].append(aft_dice)
    #             results['dice-wo-reg'].append(bef_dice)

    #             print(f'subject:{subject}', f'label_idx:{label_idx}', f'BEF-DICE:{bef_dice:.3f}', f'AFT-DICE:{aft_dice:.3f}')

    #             self.save_img(fx_seg[:, :, label_idx, ...], os.path.join(visualization_path, f'{idx+1}-fx_img_{label_idx}.nii'))
    #             self.save_img(mv_seg[:, :, label_idx, ...], os.path.join(visualization_path, f'{idx+1}-mv_img_{label_idx}.nii'))
    #             self.save_img(pred_seg[0], os.path.join(visualization_path, f'{idx+1}-pred_img_{label_idx}.nii'))


    #     for k, v in results.items():
    #         print(f'overall {k}, {np.mean(v):.3f}, {np.std(v):.3f}')
    #         if 'dice' in k or 'cd' in k:
    #             for idx in range(label_num):
    #                 tmp = v[idx::label_num]
    #                 print(f'results of {k} on label {idx}:, {np.mean(tmp):.3f} +- {np.std(tmp):.3f}')        

    #     with open(os.path.join(self.log_dir, 'results.pkl'), 'wb') as f:
    #         pkl.dump(results, f)


