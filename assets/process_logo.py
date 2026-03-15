from PIL import Image, ImageOps, ImageFilter, ImageEnhance, ImageChops
import sys
import os
from PIL import ImageDraw
from collections import deque

def remove_minor_black_components(img, threshold=128):
    """
    Finds connected components of black pixels (luminance < threshold).
    Keeps the largest component and turns all other black components to white.
    """
    width, height = img.size
    pixels = img.load()
    visited = set()
    components = []
    
    # helper to check if a pixel is 'black' and part of the visible image
    def is_black(x, y):
        r, g, b, a = pixels[x, y]
        # Check alpha and luminance (assuming grayscale RGB)
        return a > 0 and r < threshold

    for y in range(height):
        for x in range(width):
            if is_black(x, y) and (x, y) not in visited:
                # Start of a new component
                component = set()
                q = deque([(x, y)])
                visited.add((x, y))
                component.add((x, y))
                
                while q:
                    cx, cy = q.popleft()
                    # Check 4 direct neighbors
                    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nx, ny = cx + dx, cy + dy
                        if 0 <= nx < width and 0 <= ny < height:
                            if (nx, ny) not in visited and is_black(nx, ny):
                                visited.add((nx, ny))
                                component.add((nx, ny))
                                q.append((nx, ny))
                components.append(component)

    if not components:
        return img
        
    # Identify the largest component (the main body)
    largest = max(components, key=len)
    
    # Eliminate all other components by turning them white
    for comp in components:
        if comp is not largest:
            for (bx, by) in comp:
                # Set to White (255, 255, 255), preserve Alpha
                _, _, _, ca = pixels[bx, by]
                pixels[bx, by] = (255, 255, 255, ca)
                
    return img

def make_transparent_bg(source_img, is_white_ink):
    """
    Creates a transparent version of the image.
    If is_white_ink is True: White pixels stay, Black pixels become transparent.
    If is_white_ink is False: Black pixels stay, White pixels become transparent.
    Uses luminance for smooth alpha blending (anti-aliasing).
    """
    # source_img is RGBA
    # Get grayscale for luminance
    gray = source_img.convert("L")
    # Get existing alpha (circle mask)
    existing_alpha = source_img.split()[-1]
    
    # Calculate new alpha from luminance
    if is_white_ink:
        # White ink: Brightness = Opacity
        lum_alpha = gray
        fill_color = (255, 255, 255)
    else:
        # Black ink: Darkness = Opacity (invert brightness)
        lum_alpha = ImageOps.invert(gray)
        fill_color = (0, 0, 0)
    
    # Combine with existing mask: new_alpha = (lum_alpha * existing_alpha) / 255
    final_alpha = ImageChops.multiply(lum_alpha, existing_alpha)
    
    # Create a solid color image for RGB channels (prevents fringes)
    res = Image.new('RGBA', source_img.size, fill_color + (0,))
    res.putalpha(final_alpha)
    return res

def process_image(input_path, output_path):
    # Open an image file
    # Construct relative path if needed (relative to this script)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, input_path)
    output_path = os.path.join(script_dir, output_path)
    with Image.open(input_path) as img:
        # Ensure it's in RGB mode for inversion
        if img.mode == 'RGBA':
            r, g, b, a = img.split()
            rgb_image = Image.merge('RGB', (r, g, b))
            inverted_image = ImageOps.invert(rgb_image)
            # Recombine with alpha if needed, or just keep inverted RGB
            img = inverted_image
        else:
            img = ImageOps.invert(img.convert('RGB'))

        # Convert to grayscale for density processing
        img = img.convert("L")

        # Preprocessing: Apply a hard threshold first to remove faint noise
        img = img.point(lambda p: 255 if p > 30 else 0)

        # Iterative denoising and smoothing
        # This simulates a "reaction-diffusion" style cleanup or smooth thresholding
        # We blur to connect the dots into continuous fields, then apply contrast
        # to push uncertain pixels towards black or white, but keep gradients smooth.
        
        iterations = 15
        blur_radius = 10
        contrast_factor = 3 # Increase contrast gently

        for i in range(iterations):
            # Blur to merge scattered dots into shapes
            img = img.filter(ImageFilter.GaussianBlur(radius=blur_radius))
            
            # Enhance contrast to clean up noise (soft thresholding)
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast_factor)
            
            # Reduce blur radius for subsequent passes to refine edges
            blur_radius = max(0.5, blur_radius * 0.8)

        # Final pass to ensure blacks are black and whites are white without jagged edges
        # Just a little more contrast
        enhancer = ImageEnhance.Contrast(img)
        final_img = enhancer.enhance(4.0)
        # Create circular mask as large as possible
        width, height = final_img.size
        diameter = min(width, height)
        
        # Create a mask for the circle
        mask = Image.new('L', (width, height), 0)
        draw = ImageDraw.Draw(mask)
        
        # Calculate circle position to center it
        x = (width - diameter) // 2
        y = (height - diameter) // 2
        
        # Draw white circle on mask
        draw.ellipse([x, y, x + diameter, y + diameter], fill=255)
        
        # Convert grayscale to RGBA and apply mask
        final_img = final_img.convert('RGBA')
        final_img.putalpha(mask)

        # Flood-fill / Connected Component analysis to remove noise
        print("Filtering isolated noise...")
        final_img = remove_minor_black_components(final_img)

        # Save the result (PNG)
        base_filename, ext = os.path.splitext(output_path)
        final_img.save(output_path)
        print(f"Processed image saved to {output_path}")

        # Save as Icon (Standard & High Res sizes)
        icon_sizes = [(256, 256), (128, 128), (64, 64), (48, 48), (32, 32), (16, 16)]
        
        icon_path = f"{base_filename}.ico"
        final_img.save(icon_path, format='ICO', sizes=icon_sizes)
        print(f"Original icon saved to {icon_path}")

        # Create Inverted Image (White curves on Black background)
        # We split the channels, invert the color info (RGB), but keep the Alpha channel (Mask) intact.
        r, g, b, a = final_img.split()
        rgb_image = Image.merge('RGB', (r, g, b))
        inverted_rgb = ImageOps.invert(rgb_image)
        inverted_img = Image.merge('RGBA', (*inverted_rgb.split(), a))
        
        # Save Inverted PNG
        inverted_png_path = f"{base_filename}_inverted{ext}"
        inverted_img.save(inverted_png_path)
        print(f"Inverted PNG saved to {inverted_png_path}")

        # Save Inverted Icon
        inverted_icon_path = f"{base_filename}_inverted.ico"
        inverted_img.save(inverted_icon_path, format='ICO', sizes=icon_sizes)
        print(f"Inverted icon saved to {inverted_icon_path}")

        # Generate Transparent Black Version (Black Ink, Clear BG)
        trans_black = make_transparent_bg(final_img, is_white_ink=False)
        trans_black.save(f"{base_filename}_transparent{ext}")
        trans_black.save(f"{base_filename}_transparent.ico", format='ICO', sizes=icon_sizes)
        print(f"Transparent Black versions saved.")

        # Generate Transparent White Version (White Ink, Clear BG)
        trans_white = make_transparent_bg(inverted_img, is_white_ink=True)
        trans_white.save(f"{base_filename}_inverted_transparent{ext}")
        trans_white.save(f"{base_filename}_inverted_transparent.ico", format='ICO', sizes=icon_sizes)
        print(f"Transparent White versions saved.")

if __name__ == "__main__":
    process_image("logo_2.png", "logo_processed_3.png")
