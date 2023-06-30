"""
Pygame Utilities
"""
import time
import pygame

# Custom imports
from pygame_constants import *

# Initialise pygame window
WIN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
WIN.fill(BACKGROUND_COLOUR)
clock = pygame.time.Clock()

# Displays a colour at the specified LED
def drawLED(x, y, colour):
    corrected_x = (x * (PIXEL_SIZE + GAP_SIZE))
    corrected_y = WINDOW_HEIGHT - (y * (PIXEL_SIZE + GAP_SIZE)) - (PIXEL_SIZE + GAP_SIZE)
    pygame.draw.rect(WIN, (colour[0], colour[1], colour[2]), pygame.Rect(corrected_x, corrected_y, PIXEL_SIZE, PIXEL_SIZE))

mapping = {}
# Function to create the 2D array and map each pixel
def createGrid(x, y):
    n = 0
    i = y - 1
    right_direction = True
    array = [[None for i in range(x)] for j in range(y)]

    val = BOARD_WIDTH * BOARD_HEIGHT
    while i >= 0:   # Y value
        if right_direction:
            ii = 0
            while ii < x:
                array[i][ii] = val
                mapping[n] = array[i][ii]
                val -= 1
                ii += 1
                n += 1
            right_direction = False
        else:
            ii = x - 1
            while ii >= 0:
                array[i][ii] = val
                mapping[n] = array[i][ii]
                val -= 1
                n -= 1
                ii -= 1
            right_direction = True

        i -= 1

    return array

# Create a grid
map_grid = createGrid(BOARD_WIDTH, BOARD_HEIGHT)

# Getting the number of the LED when you enter X and Y coordinates
def getLED(input_x, input_y):
    if input_x > 29 or input_x < 0 or input_y > 19 or input_y < 0:
        raise ValueError(f"x and y coordinates are out of bounds: x = {input_x}, y = {input_y}")

    right_direction = True
    output = input_y * BOARD_WIDTH

    if input_y % 2 != 0:
        right_direction = False

    if right_direction:
        output += input_x
    else:
        output += ((BOARD_WIDTH - 1) - input_x)

    return output + 1

# Set all pixels to a specified colour
def setAllPixelsColour(colour):
    # Go through the total y LEDs
    for y in range(BOARD_HEIGHT+1):
        # Go through the total x LEDs
        for x in range(BOARD_WIDTH):
            # drawLED at x, y and the colour
            drawLED(x, y, colour)

    pygame.display.update()

# Set specified colour to consecutive or single pixels
def setPixelsColour(colour, pixel_index_start, pixel_index_end = None):
    if pixel_index_start > BOARD_HEIGHT * BOARD_WIDTH or pixel_index_start < 0:
        raise IndexError(f"pixel_index_start is out of the allowed range: pixel_index_start = {pixel_index_start}")
    if pixel_index_end != None:
        if pixel_index_end > BOARD_HEIGHT * BOARD_WIDTH or pixel_index_end < 0:
            raise IndexError(f"pixel_index_end is out of the allowed range: pixel_index_end = {pixel_index_end}")

    # Checks if it's one pixel or multiple that need to change
    if pixel_index_end == None:
        # Find the x and y coords of the index
        escape = False
        y = 0
        while y < len(map_grid):
            x = 0
            while x < len(map_grid[0]):
                if map_grid[y][x] == pixel_index_start:
                    escape = True
                    break
                else:
                    x += 1
            if escape == True:
                break
            y += 1
        # Change LED colour
        drawLED(x, y, colour)
    else:
        # Start loop to change all LEDs to specified colour
        while pixel_index_start != pixel_index_end + 1:
            # Find the x and y coords of the index
            escape = False
            y = 0
            while y < len(map_grid):
                x = 0
                while x < len(map_grid[0]):
                    if map_grid[y][x] == pixel_index_start:
                        escape = True
                        break
                    else:
                        x += 1
                if escape == True:
                    break
                y += 1
            # Change LED colour
            drawLED(x, y, colour)
            # Increment LED index
            pixel_index_start = pixel_index_start + 1

    # Update LEDs
    pygame.display.update()

# Dictionary for colors
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

COLOUR_MATCHES = [
    ["Dark Blue", "Green", "Black"]
]

num_to_colours = []
# Add all the colours to num_to_colours
for key in iter(COLOURS):
    num_to_colours.append(key)


# Startup function (To check there is no errors with the code)
def startup(delay):
    for key in iter(COLOURS):
        setAllPixelsColour(COLOURS[key])
        time.sleep(delay)
