"""
For graphics

Note: The coordinates start from the top left and the first LED is (0, 0)
"""
import time
import random

# Custom imports
from rpi import *
from utilities import *
from images import *

# To draw a single line between 2 points
def drawLine(pixel_framebuf, start_x, start_y, end_x, end_y, colour):
    pixel_framebuf.line(start_x, start_y, end_x, end_y, RGBToHex(colour))
    pixel_framebuf.display()

# To draw a vertical or horizontal line
def drawStraightLine(pixel_framebuf, x, y, length, colour, horizontal):
    if horizontal == True:
        # It draws the line from left to right
        pixel_framebuf.hline(x, y, length, RGBToHex(colour))
    else:
        # It draw the line from top to bottom
        pixel_framebuf.vline(x, y, length, RGBToHex(colour))

    pixel_framebuf.display()

# Draw a hollow or filled rectangle (starts from the top left corner)
def drawRect(pixel_framebuf, x, y, width, height, colour, filled):
    if filled == True:
        pixel_framebuf.fill_rect(x, y, width, height, RGBToHex(colour))
    else:
        pixel_framebuf.rect(x, y, width, height, RGBToHex(colour))

    pixel_framebuf.display()

# Draws a circle with center (x, y)
def drawCircle(pixel_framebuf, x, y, radius, colour):
    pixel_framebuf.circle(x, y, radius, colour)
    pixel_framebuf.display()

# Draw text on the screen (starts from the top left corner and can go off screen)
def drawText(pixel_framebuf, text, colour, x, y = 5):
    pixel_framebuf.text(text, x, y, RGBToHex(colour))
    pixel_framebuf.display()

# Animate text scrolling from right to left
# Note: The text will always start and end off-screen, from right to left
def scrollText(pixel_framebuf, text, colour, delay = 0.05, y = 5):
    # Start the text off-screen to the right
    start_x = BOARD_WIDTH + 1

    # Calculate the total LEDs needed until the text is off-screen to the left
    end_x = -((TEXT_WIDTH * (len(text) - text.count(" "))) + text.count(" "))

    # Scroll the text
    while start_x > end_x:
        pixels, pixel_framebuf = changeBrightness(PIXEL_BRIGHTNESS)
        drawText(pixel_framebuf, text, colour, start_x, y)
        time.sleep(delay)
        setAllPixelsColour(pixels, COLOURS["Black"])
        start_x -= 1

# Cycles randomly through a list of preset phrases
def randomiseText(pixel_framebuf, colour, scroll_delay = None):
    # Store all text in an array
    all_text = ["Hello there!"]

    # Have an empty array to store all the random numbers chosen
    chosen_numbers = []

    total_shown = 0
    while total_shown < len(all_text):
        number = random.randint(0, len(all_text) - 1)

        # If it's not already chosen
        if number not in chosen_numbers:
            scrollText(pixel_framebuf, all_text[number], colour, scroll_delay)

            chosen_numbers.append(number)

            total_shown += 1

# Tests all graphics functions
def testGraphics(delay = 1):
    drawLine(pixel_framebuf, 0, 0, 3, 2, COLOURS["Green"])
    drawStraightLine(pixel_framebuf, 4, 4, 5, COLOURS["Blue"], True)
    drawStraightLine(pixel_framebuf, 4, 4, 4, COLOURS["Blue"], False)
    drawRect(pixel_framebuf, 6, 6, 8, 8, COLOURS["Red"], False)
    drawRect(pixel_framebuf, 8, 8, 3, 3, COLOURS["Orange"], True)
    drawCircle(pixel_framebuf, 10, 10, 1, COLOURS["Green"])
    time.sleep(delay)
    setAllPixelsColour(pixels, COLOURS["Black"])
    scrollText(pixels, pixel_framebuf, "Text", COLOURS["Red"], 0.01)
    setAllPixelsColour(pixels, COLOURS["Black"])
