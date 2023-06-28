"""
Main Loop
"""
import time

# Custom imports
from rpi import *
from utilities import *
from precomputations import *
from graphics import *
from images import *
from ultrasonics import *

# Reset board
setAllPixelsColour(pixels, COLOURS["Black"])

print("Starting display.")

pixels, pixel_framebuf = changeBrightness(PIXEL_BRIGHTNESS)

# Main running loop
while True:
    checkUltrasonics()
    setAllPixelsColour(pixels, COLOURS["Black"])

    print("Calculating waves...")
    merged, non_merged = randomisePatterns()
    
    print("Displaying waves.")
    displayRandomPatterns(pixel_framebuf, merged, non_merged)

    checkUltrasonics()
