# Config Directory

The `config` directory is central to the project's modular configuration approach. It houses the configuration files for different model trainings, utilities, and the core configuration library, `configlib.py`.

## Modular Configuration Approach

The `config` directory employs a modular configuration system, allowing each model or training setup to have its own configuration file. This ensures:

1. **Scalability**: As more models or setups are introduced, new configuration files can be easily added without affecting existing configurations.
2. **Maintainability**: Each configuration file is self-contained, streamlining updates, debugging, and modifications.
3. **Reusability**: Common configurations are defined once in the `global_train_config.py` and can be reused across different configuration files.

## Dynamic Project Handling with `global_train_config.py`

The beauty of this setup is its ability to cater to multiple projects, allowing different network architectures or training procedures to be applied to different datasets seamlessly. The `global_train_config.py` file serves as a hub for this:

- **Dynamic Project Selection**: Based on the command line arguments, the file dynamically selects and imports the configurations specific to a chosen project.
- **General Configurations**: It provides general configurations that are globally applicable, like learning rate, batch size, GPU selection, etc.
- **Modularity**: With the `project_list` variable, it's easy to add or remove projects, making the system extensible.
- **Assertion Checks**: The file checks for necessary configurations like `exp_name` and `data_path`, ensuring they are provided before proceeding.

### Usage

When invoking a script, specify the `--project` flag followed by the desired project name. The system will automatically fetch the corresponding configurations.

For instance, when running a training script for the `CBCTUnetSeg` model, the script will reference the `CBCTUnetSeg_train_config.py` file for its configurations.

To see the available configurations for a specific model or setup, you can typically run the corresponding configuration file with the `-h` flag:

```bash
python3 CBCTUnetSeg_train_config.py -h
```

## Files & Descriptions

### Model-Specific Configuration Files

These files define hyperparameters and settings for different model trainings:

- `CBCTUnetSeg_train_config.py`: Configuration for the CBCTUnetSeg model training.
- `ConditionalSeg_train_config.py`: Configuration for the ConditionalSeg model training.
- `WeakSup_train_config.py`: Configuration for the WeakSup model training.

Each of these files leverages the `configlib` to declare its specific set of arguments and configurations.

### Utilities & Libraries

- `config_utils.py`: Contains utility functions that may be used across multiple configuration files, ensuring consistency and reducing redundancy.
- `configlib.py`: The core configuration library based on Python's `argparse` module. It facilitates the modular configuration approach by allowing each module to declare its arguments and ensuring global access to the parsed arguments.

### Global Configurations

- `global_train_config.py`: Contains settings and configurations that are common across all training setups. This ensures that universally applicable settings are defined in one place and can be easily referenced by any model-specific configuration file.

## Conclusion

The config directory, especially with the capabilities of global_train_config.py, ensures that the project remains flexible, organized, and easily extendable.

## References

1. Nuri Cingillioglu, "Argparse with multiple files to handle configuration in Python", [Link](https://www.doc.ic.ac.uk/~nuric/coding/argparse-with-multiple-files-to-handle-configuration-in-python.html).
