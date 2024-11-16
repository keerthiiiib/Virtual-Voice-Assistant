import tensorflow as tf
import numpy as np
from PIL import Image
import os

def generate_image():
    try:
        # Get the directory of the current script
        script_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Define the 'assets' folder path within the 'AI' directory
        assets_dir = os.path.join(script_dir, "assets")
        
        # Ensure the 'assets' folder exists
        os.makedirs(assets_dir, exist_ok=True)
        
        # Generate a pink gradient pattern for the cake background
        width, height = 256, 256
        x = np.linspace(255, 200, width, dtype=np.uint8)  # Pinkish gradient
        y = np.linspace(255, 200, height, dtype=np.uint8)
        xv, yv = np.meshgrid(x, y)

        # Apply the gradient to all RGB channels (pink shades)
        red_channel = xv
        green_channel = (xv + yv) // 4  # Lighter green for a soft touch
        blue_channel = (xv + yv) // 3  # A mix of blue for the soft kawaii effect

        # Stack the channels to create a pinkish image with a gradient effect
        image_array = np.stack([red_channel, green_channel, blue_channel], axis=-1)

        # Create the "cake" shape with a rectangle in the middle
        cake_top = (slice(80, 176), slice(80, 176))  # Middle part of the image
        image_array[cake_top] = [255, 182, 193]  # Light pink for the cake

        # Add a "whipped cream" top
        whipped_cream_top = (slice(60, 80), slice(60, 196))
        image_array[whipped_cream_top] = [255, 255, 255]  # White for the cream

        # Add a cherry on top (small red dot)
        cherry_pos = (60, 128)  # Center of the cake
        image_array[cherry_pos] = [255, 0, 0]  # Red cherry

        # Convert the array to a PIL image
        image = Image.fromarray(image_array, mode="RGB")

        # Save the generated image in the 'assets' folder
        save_path = os.path.join(assets_dir, "pink_cake_image.png")
        image.save(save_path)
        print(f"Image generated successfully! Check the file at '{save_path}'.")
    except Exception as e:
        print(f"Error generating image: {str(e)}")

