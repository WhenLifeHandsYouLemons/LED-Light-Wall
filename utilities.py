"""
Utilities
"""
import time

# Custom imports
from rpi import *

# Getting the number of the LED when you enter X and Y coordinates
def getLED(input_x, input_y):
    if input_x > BOARD_WIDTH - 1 or input_x < 0 or input_y > BOARD_HEIGHT - 1 or input_y < 0:
        raise ValueError(f"x and y coordinates are out of bounds: x = {input_x}, y = {input_y}")

    right_direction = True
    output = input_y * BOARD_WIDTH

    if input_y % 2 != 0:
        right_direction = False

    if right_direction:
        output += input_x
    else:
        output += ((BOARD_WIDTH - 1) - input_x)

    return output

def RGBToHex(colour):
    if colour[0] > 255 or colour[1] > 255 or colour[2] > 255 or colour[0] < 0 or colour[1] < 0 or colour[2] < 0:
        raise ValueError(f"The colour values are out of bounds: r = {colour[0]}, g = {colour[1]}, b = {colour[2]}")
    return int("{:02x}{:02x}{:02x}".format(colour[0], colour[1], colour[2]), 16)

# Set all pixels to a specified colour
def setAllPixelsColour(pixels, colour):
    pixels.fill(colour)
    pixels.show()

# Set specified colour to consecutive or single pixels
def setPixelsColour(pixels, colour, pixel_index_start, pixel_index_end=None):
    if pixel_index_start > BOARD_HEIGHT * BOARD_WIDTH or pixel_index_start < 0:
        raise IndexError(f"pixel_index_start is out of the allowed range: pixel_index_start = {pixel_index_start}")
    if pixel_index_end != None:
        if pixel_index_end > BOARD_HEIGHT * BOARD_WIDTH or pixel_index_end < 0:
            raise IndexError(f"pixel_index_end is out of the allowed range: pixel_index_end = {pixel_index_end}")

    # Checks if it's one pixel or multiple that need to change
    if pixel_index_end == None:
        # Change LED colour
        pixels[pixel_index_start] = colour
    else:
        # Start loop to change all LEDs to specified colour
        while pixel_index_start != pixel_index_end + 1:
            # Change LED colour
            pixels[pixel_index_start] = colour
            # Increment LED index
            pixel_index_start = pixel_index_start + 1

# Changes the brightness of the LEDs on the board
# Can also be used for resetting the frame buffer when showing text
def changeBrightness(brightness):
    pixels = neopixel.NeoPixel(
        DATA_PIN,
        BOARD_WIDTH * BOARD_HEIGHT,
        brightness=brightness,
        auto_write=False,
        pixel_order=neopixel.GRB
    )
    pixel_framebuf = PixelFramebuffer(
        pixels,
        BOARD_WIDTH,
        BOARD_HEIGHT,
        rotation=2,
        reverse_x=True,
        reverse_y=False
    )

    return pixels, pixel_framebuf

# Dictionary for colours
COLOURS = {
    "Red" : (255, 0, 0),
    "Pink" : (100, 75, 80),
    "Red Orange" : (100, 33, 29),
    "Orange" : (255, 165, 0),
    "Amber" : (100, 75, 0),
    "Yellow" : (255, 255, 0),
    "Lime": (75, 100, 0),
    "Green" : (0, 255, 0),
    "Blue Green" : (5, 60, 73),
    "Dark Green" : (0, 20, 13),
    "Light Blue" : (68, 85, 90),
    "Blue" : (0, 0, 255),
    "Dark Blue" : (0, 0, 55),
    "Blue Purple" : (54, 17, 89),
    "Purple" : (50, 0, 50),
    "Brown" : (139, 69, 19),
    "Grey" : (128, 128, 128),
    "Black" : (0, 0, 0),
    "White" : (255, 255, 255)
}

num_to_colours = []
# Add all the colours to num_to_colours
for key in iter(COLOURS):
    num_to_colours.append(key)

# Startup function (To check there is no errors with the code)
def startup(delay):
    for key in iter(COLOURS):
        setAllPixelsColour(pixels, COLOURS[key])
        time.sleep(delay)
