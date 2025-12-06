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
def adjust_saturation(img: Image.Image, factor: float) -> Image.Image:
    """
    Adjusts the intensity of colors (saturation).
    
    Factor 1.0 = original, 0.0 = grayscale, > 1.0 = more vibrant colors.
    """
    if not isinstance(img, Image.Image):
        raise TypeError("Input must be a PIL Image object.")
        
    enhancer = ImageEnhance.Color(img)
    return enhancer.enhance(factor)

# 3. SHARPNESS
def adjust_sharpness(img: Image.Image, factor: float) -> Image.Image:
    """
    Adjusts the image sharpness.
    
    Factor 1.0 = original, > 1.0 = sharper, < 1.0 = blurrier.
    """
    if not isinstance(img, Image.Image):
        raise TypeError("Input must be a PIL Image object.")
        
    enhancer = ImageEnhance.Sharpness(img)
    return enhancer.enhance(factor)




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
def apply_gritty_contrast(img: Image.Image) -> Image.Image:
    """
    Applies an 'Urban Gritty Contrast' look.
    Low saturation and crushed shadows for high contrast.
    """
    img = adjust_sharpness(img, 2.50)
    img = adjust_brightness(img, 0.90)
    img = adjust_shadows(img, -0.20)
    img = adjust_saturation(img, 0.80) 
    return img

# 3. PASTEL MATTE TEMPLATE
def apply_pastel_matte(img: Image.Image) -> Image.Image:
    """
    Applies a 'Soft Pastel Matte' look.
    Over-brightness and aggressive shadow lift for the matte look.
    """
    img = adjust_saturation(img, 1.10)
    img = adjust_shadows(img, 0.70)
    img = adjust_brightness(img, 1.20)
    img = adjust_sharpness(img, 0.90)
    return img

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


    