# Deep Learning Project Template

This project provides a structured template for deep learning research and applications in PyTorch. The organized directory structure facilitates easy navigation, maintenance, and scalability.

## Directory Structure and Descriptions

### 1. LICENSE

This file contains the licensing information for the project, specifying how others can use, modify, and distribute the code.

### 2. Tools

A collection of utility tools and scripts.

- **hpc**: Houses scripts related to High-Performance Computing. Currently, it contains:
  - `qsub.py`: A script for submitting jobs to an HPC cluster.

### 3. config

Configuration files and utilities for the project reside here.

- **Model Configurations**: Files like `PROJECTNAME_train_config.py`, etc., define hyperparameters and settings for different model trainings.

- **Utilities**: 
  - `config_utils.py`: Contains utility functions that assist with configuration display and color-coded messaging.
  - `configlib.py`: Core library functions for configuration management, inspired by this guide.
  - `global_train_config.py`: A dynamic configuration handler that allows for a modular approach to various projects. It provides general settings and configurations common across all training setups and facilitates the selection of specific project configurations based on command line arguments.

### 4. logs

This directory is reserved for storing logs generated during training, testing, or any other processes. Logs are essential for tracking the progress and performance of models.

### 5. preprocessing

Scripts and files related to data preprocessing. Generally ran on raw input data to prepare it for training and inference.

- **example_project**`/00.data_clean.py`: Script for data cleaning.


Modify the ``save_root`` and ``src_root`` in ``00.data_clean.py`` and run as follows. It will convert the nifty images into numpy array and save them in the ``save_root``. You will need to write these yourself for your own project.

```
python 00.data_clean.py
```

### 6. requirements.txt

Lists all the Python packages and their specific versions required to run the project.

### 7. scripts

Contains shell scripts for various purposes, like starting training or testing processes, especially useful in an HPC environment.

- **example_project/local**: 
  - `example_cv0.sh`: An example script for testing the `example` model with cross-validation fold set 0. Will need to be modified based on the project and model.

### 8. src

Source code directory.

- **data**: Contains code related to data handling.
  - `dataloaders.py`: Functions to load data batches.
  - `preprocess.py`: Functions for data preprocessing.
- **model**: All model-related code.
  - **archs**: Model architectures, inherit from `baseArch.py`.
  - **networks**: Network configurations or implementations, like `local.py`.
  - Utility Files: `functions.py` (general utility functions), `layers.py` (custom layers), `loss.py` (loss functions), and `metric.py` (evaluation metrics).

### 9. test.py

Script for testing trained models against validation or test datasets.

### 10. train.py

Main script to train deep learning models.

---

## Getting Started

1. **Clone the Repository**:
   Use the following command to clone the repository to your local machine:

```sh
git clone MyRepo
```

2. **Set Up the Environment**:
Navigate to the project directory and install the required packages:

```sh
cd deep-learning-project-template
python3 -m pip install -r requirements.txt
```

It is highly recommended you set up a virtual environment to manage dependencies and avoid potential conflicts:

```sh
python3 -m venv envs/PROJECTNAME_env
source envs/PROJECTNAME_env/bin/activate # On Windows use: env\Scripts\activate
python3 -m pip install -r envs/PROJECTNAME_requirements.txt
```

3. **Adjust Configurations**:
- Navigate to the `config` directory.
- Review and adjust project/model-specific configuration files of the format `PROJECTNAME_train_config.py`, based on your requirements.

- For global settings that apply to all training setups, modify `global_train_config.py`.

4. **Data Preprocessing**:
- Ensure your data is placed in the appropriate directories.
- Run preprocessing scripts from the `preprocessing` directory, such as `00.data_clean.py`, to clean and prepare your data for training.

5. **Training**:
- Use `train.py` to start training your models. Depending on your configurations, the trained models and logs will be saved in designated directories. 

- Monitor the `logs` directory for training progress and potential issues; or if you are using an experient management tool like [Weights & Biases](https://wandb.ai/site), you can monitor the training progress there.

6. **Testing & Evaluation**:
- After the training is done, you can copy the models back and do the inference in a local machine to avoid queuing. 
- The models will be saved in ``./logs/[--project]/[--exp_name]``
- Use the following command to do the inference. It will do inference on the best model if the ''[num_epoch]'' is omit.

```
python3 -m test.py ./logs/[--project_name]/[--exp_name] [gpu_id] [num_epoch]
```

7. **Explore Further**:
- Dive into the `src` directory to explore model architectures, utilities, and other functionalities.
- Use scripts from the `scripts` directory for specific tasks, especially if you're working in an HPC environment.

---

For detailed explanations or if you encounter any issues, please refer to the individual READMEs in specific directories or raise an issue in the repository.


## References

1. Nuri Cingillioglu, "Argparse with multiple files to handle configuration in Python", [Link](https://www.doc.ic.ac.uk/~nuric/coding/argparse-with-multiple-files-to-handle-configuration-in-python.html).

## Acknowledgements

This project is based on original work by Qianye Yang. The current repository serves as a template, with specific project details stripped for generalization purposes. I deeply appreciate Qianye Yang for their invaluable contributions and expertise.

You can find the original project and more of Qianye Yang's work at https://github.com/QianyeYang/mpmrireg.

