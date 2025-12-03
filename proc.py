# Import Files
from PIL import Image, ImageEnhance
import math
from typing import Generator, Tuple, Union

# General Utility
def load_image(path: str) -> Image.Image:
    """Loads an image from a file path."""
    return Image.open(path)


# --- FEATURE IMPLEMENTATION ---

# 1. BRIGHTNESS
def adjust_brightness(img: Image.Image, factor: float) -> Image.Image:
    """
    Adjusts the overall brightness of the image.
    Factor 1.0 = original, > 1.0 = brighter, < 1.0 = darker.
    """
    if not isinstance(img, Image.Image):
        raise TypeError("Input must be a PIL Image object.")
    
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(factor)


# 2. SATURATION




# 3. SHARPNESS




# 4. SHADOWS




# --- TEMPLATE FUNCTIONS ---

# 1. GOLDEN HOUR TEMPLATE

# 2. GRITTY CONTRAST TEMPLATE

# 3. PASTEL MATTE TEMPLATE

# --- MANUAL EDIT SEQUENCE ---
def process_manual_edits(
    img: Image.Image, 
    saturation_factor: float, 
    shadows_amount: float, 
    brightness_factor: float, 
    sharpness_factor: float
) -> Generator[Tuple[str, Image.Image], None, None]:
    """
    Applies the four manual edits sequentially and yields the image 
    after each step, plus the name of the feature just applied.
    
    The generator yields: (feature_name, image_object)
    """
    current_img = img.copy()

    # 1. SATURATION
    current_img = adjust_saturation(current_img, saturation_factor)
    yield ("saturation", current_img)

    # 2. SHADOWS
    current_img = adjust_shadows(current_img, shadows_amount)
    yield ("shadows", current_img)

    # 3. BRIGHTNESS
    current_img = adjust_brightness(current_img, brightness_factor)
    yield ("brightness", current_img)

    # 4. SHARPNESS
    current_img = adjust_sharpness(current_img, sharpness_factor)
    yield ("sharpness", current_img)


    