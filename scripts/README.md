# Scripts Directory

The `scripts` directory contains execution scripts tailored for various projects and computational setups. These scripts are crafted to run specific training or evaluation tasks, leveraging configurations provided in the `config` directory.

## Directory Structure

The directory is organized into multiple subdirectories, each named after a specific project. Within each project's directory, there are further subdirectories that cater to different computational setups, such as `local` for local execution or specific names for external clusters and computers.

```sh
.
└── [project_name]
└── [compute_setup]
└── [script_name].sh
```

For instance:

```sh
.
└── example_project
└── local
└── example_cv0.sh
```


## Script Structure & Usage

Each script, like `example_cv0.sh`, typically starts with a set of directives (in the case of shell scripts, these might be specific to a job scheduler like Sun Grid Engine). These directives specify the computational resources required, job naming, logging specifications, and other settings relevant to the computational environment.

The main body of the script invokes a Python training or evaluation script, such as `train.py`, passing along necessary configurations and parameters. These configurations are based on the arguments defined in the corresponding `config` files.

For example, the line:

```bash
python3 -u train.py \
--project PROJECTNAME \
```

Here, `PROJECTNAME`` would be replaced with the actual name of the project, as defined in the config directory.

## Notes

- Ensure that you replace placeholders like PROJECTNAME, EXPNAMECV0, and PATH with actual values before running the script.
- The available configuration options for each script are defined based on the `config` files. Therefore, it's essential to keep the `config` directory updated and synchronized with the `scripts` directory.

## Conclusion

The `scripts` directory serves as the entry point for executing various tasks, making use of the modular configuration approach from the `config` directory. By organizing scripts based on projects and computational setups, the structure remains clean, scalable, and easy to navigate.

