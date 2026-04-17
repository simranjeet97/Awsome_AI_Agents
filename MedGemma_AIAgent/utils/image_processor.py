import numpy as np
import pydicom
import nibabel as nib
from PIL import Image
import cv2
import io

class MedicalImageProcessor:
    @staticmethod
    def apply_window(img, window_center, window_width):
        """Standard radiological windowing."""
        img_min = window_center - window_width // 2
        img_max = window_center + window_width // 2
        windowed = np.clip(img, img_min, img_max)
        windowed = ((windowed - img_min) / window_width * 255.0).astype(np.uint8)
        return windowed

    @classmethod
    def process_ct_rgb(cls, slice_data):
        """
        Processes a CT slice into RGB channels using common medical windows.
        R: Soft Tissue (L:40, W:400)
        G: Bone (L:400, W:1800)
        B: Lung (L:-600, W:1500)
        """
        soft_tissue = cls.apply_window(slice_data, 40, 400)
        bone = cls.apply_window(slice_data, 400, 1800)
        lung = cls.apply_window(slice_data, -600, 1500)
        
        rgb = np.stack([soft_tissue, bone, lung], axis=-1)
        return rgb

    @classmethod
    def load_dicom_slice(cls, file_path):
        """Load a single DICOM slice and apply Rescale Slope/Intercept."""
        ds = pydicom.dcmread(file_path)
        img = ds.pixel_array.astype(float)
        
        # Apply rescale slope and intercept to get Hounsfield Units (HU)
        rescale_slope = getattr(ds, 'RescaleSlope', 1)
        rescale_intercept = getattr(ds, 'RescaleIntercept', 0)
        img = img * rescale_slope + rescale_intercept
        
        return img, ds

    @classmethod
    def load_nifti_volume(cls, file_path):
        """Load a NIfTI volume."""
        img = nib.load(file_path)
        data = img.get_fdata()
        return data, img.header

    @staticmethod
    def resize_for_model(img_array, target_size=(896, 896)):
        """Resize image to MedGemma's required 896x896."""
        if isinstance(img_array, Image.Image):
            return img_array.resize(target_size, Image.LANCZOS)
        
        return cv2.resize(img_array, target_size, interpolation=cv2.INTER_LANCZOS4)

    @classmethod
    def prepare_any_image(cls, image_bytes):
        """Prepare any standard 2D image format (JPG, PNG, TIFF, BMP, WebP)."""
        try:
            image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
            return cls.resize_for_model(image)
        except Exception as e:
            print(f"Error processing image: {e}")
            return None

    @classmethod
    def extract_nifti_slices(cls, file_content, num_slices=3):
        """Extract RGB slices from a NIfTI volume for MedGemma."""
        try:
            # We need to save to a temp file because nibabel expects a path
            with open("temp.nii", "wb") as f:
                f.write(file_content)
            data, header = cls.load_nifti_volume("temp.nii")
            
            # Select representative slices
            raw_slices = cls.select_slices(data, num_slices)
            processed_slices = []
            for s in raw_slices:
                # NIfTI data is often high-bit depth, similar to CT
                # We apply a generic windowing or normalization
                windowed = cls.process_ct_rgb(s) # Reuse CT windowing logic
                processed_slices.append(Image.fromarray(cls.resize_for_model(windowed)))
            return processed_slices
        except Exception as e:
            print(f"Error processing NIfTI: {e}")
            return []
