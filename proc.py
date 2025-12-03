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


    