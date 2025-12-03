# Import Files


# General Utility



# --- FEATURE IMPLEMENTATION ---

# 1. BRIGHTNESS



# 2. SATURATION




# 3. SHARPNESS




# 4. SHADOWS




# --- TEMPLATE FUNCTIONS ---

# 1. GOLDEN HOUR TEMPLATE

# 2. GRITTY CONTRAST TEMPLATE

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


    