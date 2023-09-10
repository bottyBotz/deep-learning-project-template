#$ -S /bin/bash
#$ -l tmem=11G
#$ -l gpu=true
#$ -l h_rt=96:0:0
#$ -j y
#$ -N segMCTCV0
#$ -cwd
hostname
date
python3 -u train.py \
--project PROJECTNAME \
--exp_name EXPNAMECV0 \
--data_path ../PATH \
--batch_size 8 \
--input_mode both \
--inc 2 \
--outc 2 \
--gpu 1 \
--cv 0 \
--input_shape 64 101 91 \
--lr 1e-5 \
--affine_scale 0.15 \
--save_frequency 100 \
--num_epochs 100 \
--w_dce 1.0 \
--using_HPC 0 \
--nc_initial 16 \
--two_stage_sampling 0 \
                   
                   