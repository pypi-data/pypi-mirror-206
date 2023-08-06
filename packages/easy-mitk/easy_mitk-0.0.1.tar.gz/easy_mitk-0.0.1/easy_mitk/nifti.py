import numpy as np
import nibabel as nib


def arr2nii(arr: np.ndarray, affine = np.eye(4), save_path: str = None) -> nib.Nifti1Image:
    nii = nib.Nifti1Image(arr, affine)
    if save_path:
        nib.save(nii, save_path)
    return nii
