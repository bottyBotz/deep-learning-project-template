# Preprocessing Directory

The `preprocessing` directory contains preprocessing workflows tailored for individual projects. These workflows are designed to prepare the data in a consistent and optimal format for subsequent training. Note that further preprocessing may occur during training time, especially if learnable preprocessing methods such as spatial transformation networks are used.

## Directory Structure

The directory is organized into multiple subdirectories, each corresponding to a specific project. Each project has its unique preprocessing workflow, which ensures that the data is in the correct state for training.

```sh
.
└── [project_name]
└── [preprocessing_script].py
```

For instance:

```
.
└── example_project
└── 00.baseline_data_clean.py
```

## Preprocessing Workflow

Each preprocessing script (e.g., `00.baseline_data_clean.py`) is responsible for relevant tasks. Example tasks may be:

1. **Loading Image Data**: Importing image datasets, often from formats like `.nii.gz`, and converting them to arrays for processing.
2. **Visualization Helpers**: Functions or utilities that assist in visualizing the data, such as plotting 2D slices from 3D images or overlaying annotations.
3. **Normalization**: Adjusting the range of pixel or voxel intensities in the image. For example, normalizing the image intensities to a range of 0 to 255 to ensure consistent scales across datasets.
4. **Contour Addition**: Techniques that help in identifying and highlighting regions of interest in the image by drawing contours around them. This aids in visual inspection and can be useful for delineating structures or lesions.
5. **Center Cropping**: Removing outer parts of an image to focus on a central region. This can be crucial when the region of interest is centrally located, and the peripheral regions don't add significant value.
6. **Image Resampling**: Adjusting the resolution of the images to ensure consistent voxel sizes across datasets. This is important when combining data from different sources or when working with multi-modal images.
7. **Saving Processed Data**: After preprocessing, the data is saved in suitable formats, like `.npy`, for efficient loading during the training phase.

## Conclusion

The `preprocessing` directory is pivotal in ensuring that the data is ready for the training phase. It's crucial to ensure that each project's data undergoes the required preprocessing steps to maintain consistency and data integrity throughout the machine learning workflow.
