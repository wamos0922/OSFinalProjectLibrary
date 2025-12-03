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

# --- MANUAL EDIT SEQUENCE ---


    