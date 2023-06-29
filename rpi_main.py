"""
Main Loop
"""
import time
from datetime import datetime

# Custom imports
from rpi import *
from utilities import *
from precomputations import *
from graphics import *
from images import *
from ultrasonics import *

# Returns the current time (timezone sensitive) in the format "hh:mm:ss"
def getTime():
    time = str(datetime.now()).split(" ")[1].split(".")[0]
    return time

# Returns a string of today's day
def getDay():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = datetime.weekday(datetime.now())
    return days[day]

# Reset board
setAllPixelsColour(pixels, COLOURS["Black"])

print("Starting display.")

pixels, pixel_framebuf = changeBrightness(PIXEL_BRIGHTNESS)

# Main running loop
while True:
    checkUltrasonics()

    print("Calculating waves...")
    merged, non_merged = randomisePatterns()

    print("Displaying waves.")
    displayRandomPatterns(pixel_framebuf, merged, non_merged)
    setAllPixelsColour(pixels, COLOURS["Black"])
