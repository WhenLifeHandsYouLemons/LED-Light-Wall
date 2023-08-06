"""
For images

Note: The images have to be the same aspect ratio as the board to display properly.
"""
import time
import os
import random
from PIL import Image

# Custom imports
from rpi import *

def displayImage(pixel_framebuf, image_path, blend = False, lock_aspect = False):
    image = Image.open(image_path)
    # Resize the image to fit the board
    if lock_aspect:
        image = image.thumbnail((BOARD_WIDTH, BOARD_WIDTH))
    else:
        image = image.resize((BOARD_WIDTH, BOARD_HEIGHT))

    if blend:
        background = Image.new("RGBA", (BOARD_WIDTH, BOARD_HEIGHT))
        background.alpha_composite(image)
        pixel_framebuf.image(background.convert("RGB"))
    else:
        pixel_framebuf.image(image.convert("RGB"))

    pixel_framebuf.display()

# Cycle through random images
def randomiseImage(pixel_framebuf, invalid_numbers, delay = 1):
    # Get all the image paths in the images directory
    image_dir = "images/"
    all_images = [f"{image_dir}{img}" for img in os.listdir(image_dir)]

    # Choose a random image
    number = random.randint(0, len(all_images) - 1)
    while number in invalid_numbers:
        number = random.randint(0, len(all_images) - 1)

    displayImage(pixel_framebuf, all_images[number], lock_aspect=True)
    time.sleep(delay)

    # Return the number so that it can be removed from being chosen again
    return number
