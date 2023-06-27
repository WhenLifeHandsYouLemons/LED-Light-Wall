"""
Raspberry Pi Initialisation
"""
# To use these, follow this guide: https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage
import board
import neopixel
# To use these, follow this guide: https://learn.adafruit.com/easy-neopixel-graphics-with-the-circuitpython-pixel-framebuf-library/import-and-setup
from adafruit_pixel_framebuf import PixelFramebuffer

# Setting constants
DATA_PIN = board.D18
BOARD_WIDTH = 30
BOARD_HEIGHT = 20
PIXEL_BRIGHTNESS = 1
TEXT_WIDTH = 7

# Initialise NeoPixel grid
pixels = neopixel.NeoPixel(
    DATA_PIN,
    BOARD_WIDTH * BOARD_HEIGHT,
    brightness=PIXEL_BRIGHTNESS,    # Brightness out of 1
    auto_write=False,
    pixel_order=neopixel.GRB
)

# Initialise framebuffer for displaying graphics easily
pixel_framebuf = PixelFramebuffer(
    pixels,
    BOARD_WIDTH,
    BOARD_HEIGHT,
    rotation=2,
    reverse_x=True,
    reverse_y=False
)
