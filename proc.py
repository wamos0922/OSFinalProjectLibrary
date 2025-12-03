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
def adjust_shadows(img: Image.Image, amount: float) -> Image.Image:
    """
    Lifts or darkens the shadow areas (darkest pixels) without affecting 
    the brightest areas significantly. Positive amount lifts shadows.
    """
    if not isinstance(img, Image.Image):
        raise TypeError("Input must be a PIL Image object.")
        
    img = img.convert("RGB")
    
    def shadow_curve(x):
        # Applies a gamma-like curve only to dark pixels (for shadows)
        x_norm = x / 255.0
        # Ensure the amount is clipped to prevent extreme gamma values
        gamma_exponent = max(-2.0, min(2.0, -amount))
        gamma = math.pow(2, gamma_exponent) 
        result_norm = math.pow(x_norm, gamma)
        return int(result_norm * 255)

    lut = [shadow_curve(i) for i in range(256)]
    
    # Apply the custom lookup table to all three RGB channels
    return img.point(lut * 3)


# --- TEMPLATE FUNCTIONS ---

# 1. GOLDEN HOUR TEMPLATE

# 2. GRITTY CONTRAST TEMPLATE

# 3. PASTEL MATTE TEMPLATE

# --- MANUAL EDIT SEQUENCE ---


    