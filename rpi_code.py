"""
Imports
"""
import os
import time
import copy
import random
import math

# To use these, follow this guide: https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage
import board
import neopixel

# To use these, follow this guide: https://learn.adafruit.com/easy-neopixel-graphics-with-the-circuitpython-pixel-framebuf-library/import-and-setup
from adafruit_pixel_framebuf import PixelFramebuffer
from PIL import Image

# For the ultrasonic sensors
from gpiozero import DistanceSensor
# https://gpiozero.readthedocs.io/en/stable/api_input.html
# Don't put the GPIO pins to the SDA and SCL on the RPi, it should be on the normal GPIO pins
sensor1 = DistanceSensor(echo=17, trigger=27)
sensor2 = DistanceSensor(echo=22, trigger=24)
sensor3 = DistanceSensor(echo=26, trigger=6)
sensor4 = DistanceSensor(echo=5, trigger=16)
# Variables for 2d positioning
MAX_CHANGE = 0.25

"""
Initialisation
"""
# Values for initialising NeoPixels
DATA_PIN = board.D18
BOARD_WIDTH = 30
BOARD_HEIGHT = 20
PIXEL_BRIGHTNESS = 1

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


"""
Utilities
"""
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
def setPixelsColour(colour, pixel_index_start, pixel_index_end=None):
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


"""
For precomputation of graphics

Note: The coordinates start from the bottom left and the first LED is (0, 0)
"""
# Wave function that computes every tick of the wave and returns an array
# Note: A duration of over 60 gets increasingly slower to compute
def precomputeRipple(x, y, duration):   # duration is how many ticks the wave goes for (starts from 1)
    # Each top-level item is each tick of the wave
    # Each array in the top-level is the list of LEDs that have to be turned on for that tick
    # Each LED contains an array that has its x and y coordinates
    # Example = precomputed_wave = [
    #                               [[LED1_x, LED1_y]],
    #                               [[LED2_x, LED2_y], [LED3_x, LED3_y]],
    #                               [[LED4_x, LED4_y], [LED5_x, LED5_y], [LED6_x, LED6_y]],
    #                               [[LED7_x, LED7_y], [LED8_x, LED8_y], [LED9_x, LED9_y]]
    # ]
    precomputed_wave = []

    # First tick is hardcoded
    precomputed_wave.append([[x, y]])

    # Store every LED coordinate that has been used for easier searching
    used_leds = [[x, y]]

    # For every tick needed (value of duration)
    for tick in range(1, duration):   # Starts from 1 as we already know what tick 0 is
        tick_array = []
        # Get the previous tick array to calculate next tick
        previous_tick_array = precomputed_wave[tick-1]

        # For every LED in the previous tick array
        for i in previous_tick_array:
            # Get the separate x and y values to change it
            i_x = i[0]
            i_y = i[1]

            # Check if the LED to the left of it is in any of the previous arrays
            if [i_x - 1, i_y] not in used_leds and i_x - 1 >= 0:
                # Add it to tick_array
                tick_array.append([i_x - 1, i_y])
                # Add to used_leds
                used_leds.append([i_x - 1, i_y])

            # Check if the LED to the right of it is in any of the previous arrays
            if [i_x + 1, i_y] not in used_leds and i_x + 1 < BOARD_WIDTH:
                # Add it to tick_array
                tick_array.append([i_x + 1, i_y])
                # Add to used_leds
                used_leds.append([i_x + 1, i_y])
                # If not, then add that to the tick_array

            # Check if the LED above it is in any of the previous arrays
            if [i_x, i_y + 1] not in used_leds and i_y + 1 < BOARD_HEIGHT:
                # Add it to tick_array
                tick_array.append([i_x, i_y + 1])
                # Add to used_leds
                used_leds.append([i_x, i_y + 1])

            # Check if the LED under it is in any of the previous arrays
            if [i_x, i_y - 1] not in used_leds and i_y - 1 >= 0:
                # Add it to tick_array
                tick_array.append([i_x, i_y - 1])
                # Add to used_leds
                used_leds.append([i_x, i_y - 1])

        # Add tick_array to precomputed_wave
        precomputed_wave.append(tick_array)

    return precomputed_wave

# Precomputes a true circular wave (using the Bresenham Circle Algorithm)
def precomputeCircularWave(x, y, duration):
    precomputed_wave = []
    offset_x, offset_y = x, y

    # Hard-code the first tick
    precomputed_wave.append([[x, y]])

    # Go through the number of ticks needed
    for tick in range(1, duration):
        first_oct = []
        tick_array = []

        x = 0
        y = tick
        d = 3 - 2 * tick

        while x <= y:
            # Print out the coordinates in all eight octants
            first_oct.append([x, y])

            # Update x and y based on the Bresenham circle algorithm
            x += 1
            if d < 0:
                d = d + 4 * x + 6
            else:
                d = d + 4 * (x - y) + 10
                y -= 1

        # Add the first octant and all other octants to the tick_array
        for LED in first_oct:
            tick_array.append([offset_x + LED[0], offset_y + LED[1]])
            tick_array.append([offset_x - LED[0], offset_y + LED[1]])
            tick_array.append([offset_x + LED[0], offset_y - LED[1]])
            tick_array.append([offset_x - LED[0], offset_y - LED[1]])
            tick_array.append([offset_x + LED[1], offset_y + LED[0]])
            tick_array.append([offset_x - LED[1], offset_y + LED[0]])
            tick_array.append([offset_x + LED[1], offset_y - LED[0]])
            tick_array.append([offset_x - LED[1], offset_y - LED[0]])

        # Clear duplicate LEDs
        i = 0
        while i < len(tick_array):
            j = i + 1
            while j < len(tick_array):
                if tick_array[i] == tick_array[j]:
                    tick_array.pop(j)
                else:
                    j += 1
            i += 1

        # Add tick_array to precomputed_wave
        precomputed_wave.append(tick_array)

    return precomputed_wave

# Output should be in the same format of precomputeRipple so that precomputeColours can be used on this
def precomputeWave(pos, duration):
    # Pos:
    #   0 = Up to down
    #   1 = Right to left
    #   2 = Down to up
    #   3 = Left to right
    if (pos == 0 or pos == 2) and duration > 20:
        duration = 20
    if (pos == 1 or pos == 3) and duration > 30:
        duration = 30
    precomputed_wave = [[]]
    if pos == 0:
        x = 0
        while x < 30:
            precomputed_wave[0].append([x, 19])
            x += 1
    elif pos == 1:
        y = 0
        while y < 20:
            precomputed_wave[0].append([29, y])
            y += 1
    elif pos == 2:
        x = 0
        while x < 30:
            precomputed_wave[0].append([x, 0])
            x += 1
    elif pos == 3:
        y = 0
        while y < 20:
            precomputed_wave[0].append([0, y])
            y += 1

    for tick in range(0, duration):
        tick_array = []
        # Get the previous tick array to calculate next tick
        previous_tick_array = precomputed_wave[tick]

        # For every LED in the previous tick array
        for i in previous_tick_array:
            # Get the separate x and y values to change it
            i_x = i[0]
            i_y = i[1]

            if pos == 0:
                tick_array.append([i_x, i_y - 1])
            elif pos == 1:
                tick_array.append([i_x - 1, i_y])
            elif pos == 2:
                tick_array.append([i_x, i_y + 1])
            elif pos == 3:
                tick_array.append([i_x + 1, i_y])
        # Add tick_array to precomputed_wave
        precomputed_wave.append(tick_array)

    return precomputed_wave

# Precompute a singluar rain drop pattern which can be extended by precomputeColours
def precomputeRain(x): # x: x position
    duration = 20
    y = 19
    precomputed_wave = [[]]
    precomputed_wave[0].append([x, y])
    i = 0
    while i < duration - 1:
        y -= 1
        precomputed_wave.append([[x, y]])
        i += 1
    return precomputed_wave

# Precompute a singular, straight line
def precomputeLines(x, y, e_x, e_y, width): # Parameters: x, y: Initial center coordinantes. e_x, e_y: The end center coordinate (controls direction of line). Width: width of line
    precomputed_wave = [[]]
    dx = e_x - x
    dy = e_y - y
    m = dy / dx # m = gradient

    # y = mx + c
    c = y - (m * x) # c = y int

    if (math.fabs(dx) > math.fabs(dy)):
        skew = True
        # True = m < 1
    else:
        skew = False
        # False = m > 1

    if skew:
        i = 0
        check = 1
        if x > e_x:
            check = -1
        for x in range(x, e_x, check):
            w_count = width - 1

            y = (m * x) + c
            precomputed_wave.append([[int(x), int(y)]])

            while w_count > 0:
                n_x = x - (math.floor((width - w_count)/2))
                n_y = y - (math.ceil((width - w_count)/2))
                precomputed_wave[-1].append([int(n_x), int(n_y)])
                w_count -= 1

            i += 1
    else:
        i = 0
        check = 1
        if y > e_y:
            check = -1
        for y in range(y, e_y, check):
            w_count = width - 1
            x = (y - c) / m
            precomputed_wave.append([[int(x), int(y)]])

            while w_count > 0:
                n_x = x + (math.ceil((width - w_count)/2))
                n_y = y + (math.floor((width - w_count)/2))

                precomputed_wave[-1].append([int(n_x), int(n_y)])
                w_count -= 1

            i += 1

    return precomputed_wave

# Extend the precompute array into a 4D array with crest colors and fade colors
def precomputeColours(input_wave, i_color, e_color, fade):
    # Create array copy to not change original values
    precomputed_wave = copy.deepcopy(input_wave)

    # Calculate crest colors as it shifts
        # Calculate the shift in color each tick
    if i_color[0] < e_color[0]:
        r_shift_per_tick = (e_color[0] - i_color[0]) / (len(precomputed_wave) - 1)
        r_direction = 0
    else:
        r_shift_per_tick = (i_color[0] - e_color[0]) / (len(precomputed_wave) - 1)
        r_direction = 1

    if i_color[1] < e_color[1]:
        g_shift_per_tick = (e_color[1] - i_color[1]) / (len(precomputed_wave) - 1)
        g_direction = 0
    else:
        g_shift_per_tick = (i_color[1] - e_color[1]) / (len(precomputed_wave) - 1)
        g_direction = 1

    if i_color[2] < e_color[2]:
        b_shift_per_tick = (e_color[2] - i_color[2]) / (len(precomputed_wave) - 1)
        b_direction = 0
    else:
        b_shift_per_tick = (i_color[2] - e_color[2]) / (len(precomputed_wave) - 1)
        b_direction = 1

    # Extend the array to include crest colors
    tick_count = 0
    for tick in precomputed_wave:
        if r_direction == 0:
            r = i_color[0] + (r_shift_per_tick * tick_count)
        else:
            r = i_color[0] - (r_shift_per_tick * tick_count)
        if g_direction == 0:
            g = i_color[1] + (g_shift_per_tick * tick_count)
        else:
            g = i_color[1] - (g_shift_per_tick * tick_count)
        if b_direction == 0:
            b = i_color[2] + (b_shift_per_tick * tick_count)
        else:
            b = i_color[2] - (b_shift_per_tick * tick_count)

        for LED in tick:
            LED.append([int(r), int(g), int(b)])
        tick_count += 1


    # Fade
        # Add additional ticks with invisible crests (for trailing fade once crest deteriorates)
    i = 0
    while i < fade:
        precomputed_wave.append([])
        i += 1

    # Calculate fade and add LED items accordingly to the end of each tick
    faded_LEDS = []
    for i in precomputed_wave:
        faded_LEDS.append([])

    tick_count = 0
    for tick in precomputed_wave:
        if tick_count > 0:
            broken = False
            for i in range(1, fade+1):
                if (tick_count - i) < 0:
                    broken = True
                    break

                for LED in precomputed_wave[tick_count - i]:
                    rtemp = LED[2][0]
                    gtemp = LED[2][1]
                    btemp = LED[2][2]

                    if r_direction == 0:
                        LED[2][0] = LED[2][0] + (i * ((e_color[0] - LED[2][0] ) / fade))
                    else:
                        LED[2][0] = LED[2][0] - (i * ((LED[2][0] - e_color[0]) / fade))

                    if g_direction == 0:
                        LED[2][1] = LED[2][1] + (i * ((e_color[1] - LED[2][1] ) / fade))
                    else:
                        LED[2][1] = LED[2][1] - (i * ((LED[2][1] - e_color[1]) / fade))

                    if b_direction == 0:
                        LED[2][2] = LED[2][2] + (i * ((e_color[2] - LED[2][2] ) / fade))
                    else:
                        LED[2][2] = LED[2][2] - (i * ((LED[2][2] - e_color[2]) / fade))

                    faded_LEDS[tick_count].append(copy.deepcopy(LED))

                    LED[2][0] = rtemp
                    LED[2][1] = gtemp
                    LED[2][2] = btemp

        tick_count += 1

    tick_count = 0
    for i in faded_LEDS:
        if tick_count > 0:
            for ii in i:
                precomputed_wave[tick_count].append(ii)

        tick_count += 1

    # Add all previous tick's LEDs without changing colour to have accurate colour mixing
    start_tick = len(precomputed_wave) - 1
    while start_tick >= fade:
        # Go through every tick from 0 to start_tick-fade
        for tick_no in range(start_tick - fade):
            # Go through every LED
            for LED in precomputed_wave[tick_no]:
                if LED not in precomputed_wave[start_tick]:
                    # Add the LED to the start_tick
                    precomputed_wave[start_tick].append([LED[0], LED[1], list(e_color)])

        start_tick -= 1

    return precomputed_wave

# This takes an array of wave arrays and merges it into one master array to be displayed
def mergeWaves(wave_arrays, wave_starts):
    # Go through each wave_array and add empty ticks to the start of the wave depending on the specific wave_start
    wave_no = 0
    while wave_no < len(wave_arrays):
        for i in range(wave_starts[wave_no]):
            wave_arrays[wave_no].insert(0, [])
        wave_no += 1

    # Find the longest number of ticks
    total_ticks = 0
    for wave in wave_arrays:
        if len(wave) > total_ticks:
            total_ticks = len(wave)


    # Make all waves have the same number of ticks
    for wave in wave_arrays:
        while len(wave) != total_ticks:
            wave.append(wave[-1])

    # Sort all the LEDs for every wave into one singular array by ticks.
    sorted_wave_array = []
    for tick in range(total_ticks):
        temp_tick = []

        # Go through each wave
        for wave in wave_arrays:
            for LED in wave[tick]:
                temp_tick.append(LED)

        sorted_wave_array.append(temp_tick)

    # Hashing function for hash table
    def hasher(x, y):
        return x + y

    no_buckets = BOARD_HEIGHT + BOARD_WIDTH

    # Merge all duplicates in each tick separately
    merged_wave_array = []
    used_coords = [[] for i in range(no_buckets)]
    tick = 0
    while tick < len(sorted_wave_array):
        # Get the current led coords
        current_led_no = 0
        temp_tick = []
        used_coords = [[] for i in range(no_buckets)]

        while current_led_no < len(sorted_wave_array[tick]):
            bucket_val = hasher(sorted_wave_array[tick][current_led_no][0], sorted_wave_array[tick][current_led_no][1])

            if [sorted_wave_array[tick][current_led_no][0], sorted_wave_array[tick][current_led_no][1]] not in used_coords[bucket_val]:
                # Go through all the coords in the current tick
                check_led_no = current_led_no + 1
                total_leds = 1
                total_colour = sorted_wave_array[tick][current_led_no][2].copy()
                used_coords[bucket_val].append([sorted_wave_array[tick][current_led_no][0], sorted_wave_array[tick][current_led_no][1]])

                while check_led_no < len(sorted_wave_array[tick]):
                    # If current coords same as checking coords
                    if sorted_wave_array[tick][check_led_no][0:2] == sorted_wave_array[tick][current_led_no][0:2]:
                        # Add to total colour
                        total_colour[0] += sorted_wave_array[tick][check_led_no][2][0]
                        total_colour[1] += sorted_wave_array[tick][check_led_no][2][1]
                        total_colour[2] += sorted_wave_array[tick][check_led_no][2][2]

                        # Increment total leds
                        total_leds += 1
                    check_led_no += 1

                # Get average of total
                total_colour[0] = int(total_colour[0] / total_leds)
                total_colour[1] = int(total_colour[1] / total_leds)
                total_colour[2] = int(total_colour[2] / total_leds)

                temp_tick.append([sorted_wave_array[tick][current_led_no][0], sorted_wave_array[tick][current_led_no][1], total_colour])

            current_led_no += 1
        merged_wave_array.append(temp_tick)

        tick += 1
    return merged_wave_array

# This can take a wave array which includes colour information
def changeWaveSpeed(wave_array, ratio = 1):
    new_wave = []

    # Raise an error if it's not a positive value
    if ratio < 0:
        raise ValueError(f"The ratio for wave speed change is out of bounds: ratio = {ratio}")
    elif ratio < 1:
        # To slow down the wave
        duplicate_times = int(round(1 / ratio, 0))

        for tick in wave_array:
            for i in range(duplicate_times):
                new_wave.append(tick)
    else:
        # To speed up the wave
        i = len(wave_array) - 1
        remove_count = 0

        while i >= 0:
            if remove_count == ratio - 1:
                remove_count = 0
            else:
                wave_array.pop(i)
                remove_count += 1

            i -= 1

        new_wave = copy.deepcopy(wave_array)

    return new_wave

# This takes a wave array (can be merged or just a single wave array)
# The wave_array has to be a 4d array (includes colour information)
def displayWave(wave_array, delay = 0):
    for tick in wave_array:
        for LED in tick:
            # Change all colour values to integers to stop any float errors
            LED[2][0] = int(LED[2][0])
            LED[2][1] = int(LED[2][1])
            LED[2][2] = int(LED[2][2])
            setPixelsColour(LED[2], getLED(LED[0], LED[1]))

        pixels.show()
        time.sleep(delay)


"""
For graphics

Note: The coordinates start from the top left and the first LED is (0, 0)
"""
# To draw a single line between 2 points
def drawLine(start_x, start_y, end_x, end_y, colour):
    pixel_framebuf.line(start_x, start_y, end_x, end_y, RGBToHex(colour))
    pixel_framebuf.display()

# To draw a vertical or horizontal line
def drawStraightLine(x, y, length, colour, horizontal):
    if horizontal == True:
        # It draws the line from left to right
        pixel_framebuf.hline(x, y, length, RGBToHex(colour))
    else:
        # It draw the line from top to bottom
        pixel_framebuf.vline(x, y, length, RGBToHex(colour))

    pixel_framebuf.display()

# Draw a hollow or filled rectangle (starts from the top left corner)
def drawRect(x, y, width, height, colour, filled):
    if filled == True:
        pixel_framebuf.fill_rect(x, y, width, height, RGBToHex(colour))
    else:
        pixel_framebuf.rect(x, y, width, height, RGBToHex(colour))

    pixel_framebuf.display()

# Draws a circle with center (x, y)
def drawCircle(x, y, radius, colour):
    pixel_framebuf.circle(x, y, radius, colour)
    pixel_framebuf.display()

# Draw text on the screen (starts from the top left corner and can go off screen)
def drawText(text, colour, x, y = 5):
    pixel_framebuf.text(text, x, y, RGBToHex(colour))
    pixel_framebuf.display()

# Animate text scrolling from right to left
# Note: The text will always start from off-screen to the right and go to the left
def scrollText(text, colour, wait_time, end_x, y = 5):
    start_x = BOARD_WIDTH + 1
    while start_x > end_x:
        drawText(text, colour, start_x, y)
        time.sleep(wait_time)
        setAllPixelsColour(COLOURS["Black"])
        start_x -= 1

# Cycles randomly through a list of preset phrases
def randomiseText(colour, delay, scroll_delay):
    # Store all text in an array
    all_text = ["Hello there!"]

    # Have an empty array to store all the random numbers chosen
    chosen_numbers = []

    total_shown = 0
    while total_shown < len(all_text):
        number = random.randint(0, len(all_text))

        # If it's not already chosen
        if number not in chosen_numbers:
            # Calculate end_x for the length of the current string
            end_x = -(len(all_text[number]) * 6)

            scrollText(all_text[number], colour, scroll_delay, end_x)

            chosen_numbers.append(number)
            time.sleep(delay)

            total_shown += 1

def testGraphics(delay = 1):
    drawLine(0, 0, 3, 2, COLOURS["Green"])
    drawStraightLine(4, 4, 5, COLOURS["Blue"], True)
    drawStraightLine(4, 4, 4, COLOURS["Blue"], False)
    drawRect(6, 6, 8, 8, COLOURS["Red"], False)
    drawRect(8, 8, 3, 3, COLOURS["Orange"], True)
    drawCircle(10, 10, 1, COLOURS["Green"])
    time.sleep(delay)
    setAllPixelsColour(COLOURS["Black"])
    scrollText("Text", -100, 5, COLOURS["Red"], 0.01)
    setAllPixelsColour(COLOURS["Black"])




# Abscract for random_pattern():
# The main idea of this function is to run it once every iteration in the running while loop (which runs forever)
    # and have it continiously output patterns, only to be interrupted using if statements when:
        # 1. Ultrasonics sense something and it goes into the hand tracking ripple/circularWave
        # 2. When the time isn't when people will be using it; eg: at night, where it will be turned off.

# Displays multiple wave patterns with random colours, positions, durations, and more
def random_pattern():
    n = 9 # n = number of unique patterns
    num_of_patterns = random.randint(1, 3)
    max_fade = 7
    max_duration = 30
    if num_of_patterns == 3:
        max_fade = 7
        max_duration = 20
    i = 0

    # Log to contain all instances of waves to merge at the end
    log = []

    # Log of position of ripples/circular waves so they don't overly overlap
    pos = []

    # Cycle through color wheel for complementary colors
    color = random.randint(0, len(COLOUR_MATCHES) - 4)

    while i < num_of_patterns:
        pattern = random.randint(1, n)
        # Wave
        if pattern == 1:
            coords = random.randint(0, 3)
            duration = random.randint(15, max_duration)
            wave = precomputeWave(coords, duration)
            # check = True

            # Randomize color
            # d = dice to have chance of outlying colors of brown, grey, black and white
            d_max = 15
            d = random.randint(1, d_max)
            if d == d_max:
                i_color = len(COLOURS)
            elif d == d_max - 1:
                i_color = len(COLOURS) - 1
            elif d == d_max - 2:
                i_color == len(COLOURS) - 2
            else:
                i_color = color
                if d == 2 or d == 3: # To skip some colors, for variance
                    color += d
                else:
                    color += 1
                # Reset back to 0
                if color > len(COLOUR_MATCHES) - 4:
                    color = 0 + (color - (len(COLOUR_MATCHES) - 4))
            
            # Set ending color to always be black
            e_color = len(COLOURS) - 1

            fade = random.randint(1, max_fade)

            wave = precomputeColours(wave, COLOURS[num_to_colours[i_color]], COLOURS[num_to_colours[e_color]], fade)
            log.append(wave)

        # Ripple
        elif pattern == 2:

            # Randomize duration
            duration = random.randint(3, max_duration)
            # Randomize position
            x = random.randint(0, 29)
            y = random.rantint(0, 19)

            # Check that positioning of the origin is 'Unique'- the difference in positioning must be greater than 4 LEDs
            check = False
            for ii in pos:
                dx = math.fabs(x - ii[0])
                dy = math.fabs(y - ii[1])
                if (dx < 4 or dy < 4):
                    check = True
            while check:
                x = random.randint(0, 29)
                y = random.randint(0, 19)
                check = False
                for ii in pos:
                    dx = math.fabs(x - ii[0])
                    dy = math.fabs(y - ii[1])
                    if (dx < 4 or dy < 4):
                        check = True

            wave = precomputeRipple(x, y, duration)
            pos.append([x, y])

            # Randomize color
            # d = dice to have chance of outlying colors of brown, grey, black and white
            d_max = 15
            d = random.randint(1, d_max)
            if d == d_max:
                i_color = len(COLOURS)
            elif d == d_max - 1:
                i_color = len(COLOURS) - 1
            elif d == d_max - 2:
                i_color == len(COLOURS) - 2
            else:
                i_color = color
                if d == 2 or d == 3: # To skip some colors, for variance
                    color += d
                else:
                    color += 1
                # Reset back to 0
                if color > len(COLOUR_MATCHES) - 4:
                    color = 0 + (color - (len(COLOUR_MATCHES) - 4))

            # Set ending color to always be black
            e_color = len(COLOURS) - 1

            fade = random.randint(1, max_fade)

            wave = precomputeColours(wave, COLOURS[num_to_colours[i_color]], COLOURS[num_to_colours[e_color]], fade)
            log.append(wave)
        
        # Rain
        elif pattern == 3:
            num_of_drops = random.randint(3, 10)
            d_max = 15
            # Blue Green to Blue Purple; Skew to more 'rain-like colors'
            d = random.randint(1, d_max)
            if d == 1:
                i_color = 9
            elif d == 2:
                i_color = 10
            elif d == 3:
                i_color = 11
            elif d == 4:
                i_color = 12
            elif d == 5:
                i_color = 13
            elif d == 6:
                i_color = 14
            else:
                i_color = color
                if d == 2 or d == 3: # To skip some colors, for variance
                    color += d
                else:
                    color += 1
                # Reset back to 0
                if color > len(COLOUR_MATCHES) - 4:
                    color = 0 + (color - (len(COLOUR_MATCHES) - 4))

            
            # Set ending color to always be black
            e_color = len(COLOURS) - 1

            temp_pos = []

            ii = 0
            while i < num_of_drops:
                # Ensure that the same x position doesn't repeat
                check = False
                while check == False:
                    check = True
                    x = random.randint(0, 29)
                    for iii in temp_pos:
                        if iii == x:
                            check = False
                fade = random.randint(1, max_fade)
                wave = precomputeRain(x)
                wave = precomputeColours(wave, COLOURS[num_to_colours[i_color]], COLOURS[num_to_colours[e_color]], fade)

                temp_pos.append(x)
                log.append(wave)

        # Lines
        elif pattern == 4:
            # Randomize width of line
            width = random.randint(1, 5)

            # Randomize start of line
            x = random.randint(0, 29)
            y = random.rantint(0, 19)

            # Check that positioning of the origin is 'Unique'- the difference in positioning must be greater than 4 LEDs
            check = False
            for ii in pos:
                dx = math.fabs(x - ii[0])
                dy = math.fabs(y - ii[1])
                if (dx < 4 or dy < 4):
                    check = True
            while check:
                x = random.randint(0, 29)
                y = random.randint(0, 19)
                check = False
                for ii in pos:
                    dx = math.fabs(x - ii[0])
                    dy = math.fabs(y - ii[1])
                    if (dx < 4 or dy < 4):
                        check = True

            # Randomize end of line
            e_x = random.randint(0, 29)
            e_y = random.rantint(0, 19)

            # Check that positioning of the origin is 'Unique'- the difference in positioning must be greater than 4 LEDs
            check = False
            for ii in pos:
                dx = math.fabs(e_x - ii[0])
                dy = math.fabs(e_y - ii[1])
                if (dx < 4 or dy < 4):
                    check = True
            while check:
                e_x = random.randint(0, 29)
                e_y = random.randint(0, 19)
                check = False
                for ii in pos:
                    dx = math.fabs(e_x - ii[0])
                    dy = math.fabs(e_y - ii[1])
                    if (dx < 4 or dy < 4):
                        check = True

            d = random.randint(10)
            i_color = color
            if d == 2 or d == 3: # To skip some colors, for variance
                    color += d
            else:
                color += 1
            # Reset back to 0
            if color > len(COLOUR_MATCHES) - 4:
                color = 0 + (color - (len(COLOUR_MATCHES) - 4))

            
            # Set ending color to always be black
            e_color = len(COLOURS) - 1

            wave = precomputeLines(x, y, e_x, e_y, width)
            fade = random.randint(1, max_fade)
            wave = precomputeColours(wave, COLOURS[num_to_colours[i_color]], COLOURS[num_to_colours[e_color]], fade)

            pos.append([x, y])
            pos.append([e_x, e_y])
            log.append(wave)


        # Circle
        elif pattern == 5:
            # Randomize duration
            duration = random.randint(3, max_duration)
            # Randomize position
            x = random.randint(0, 29)
            y = random.rantint(0, 19)

            # Check that positioning of the origin is 'Unique'- the difference in positioning must be greater than 4 LEDs
            check = False
            for ii in pos:
                dx = math.fabs(x - ii[0])
                dy = math.fabs(y - ii[1])
                if (dx < 4 or dy < 4):
                    check = True
            while check:
                x = random.randint(0, 29)
                y = random.randint(0, 19)
                check = False
                for ii in pos:
                    dx = math.fabs(x - ii[0])
                    dy = math.fabs(y - ii[1])
                    if (dx < 4 or dy < 4):
                        check = True

            wave = precomputeCircularWave(x, y, duration)
            pos.append([x, y])

            # Randomize color
            # d = dice to have chance of outlying colors of brown, grey, black and white
            d_max = 15
            d = random.randint(1, d_max)
            if d == d_max:
                i_color = len(COLOURS)
            elif d == d_max - 1:
                i_color = len(COLOURS) - 1
            elif d == d_max - 2:
                i_color == len(COLOURS) - 2
            else:
                i_color = color
                if d == 2 or d == 3: # To skip some colors, for variance
                    color += d
                else:
                    color += 1
                # Reset back to 0
                if color > len(COLOUR_MATCHES) - 4:
                    color = 0 + (color - (len(COLOUR_MATCHES) - 4))

            # Set ending color to always be black
            e_color = len(COLOURS) - 1

            fade = random.randint(1, max_fade)

            wave = precomputeColours(wave, COLOURS[num_to_colours[i_color]], COLOURS[num_to_colours[e_color]], fade)
            log.append(wave)
        

        # elif pattern == 6:
            # Text
        # elif pattern == 7:
            # Image
        # elif pattern == 8:
            # More stuff


        # Lemon guy: Do the randomizer for the stuff you did like the words images ect...
        # Since your functions can't merge with other stuff, you might want to make an encapsulating if statement at the start,
        # with like a 2/num_of_total_patterns chance of it being text or an image or whatever other functions you made 

        # Note: I haven't had the chance to debug this at all, and problably won't have the chance to. Have fun.
        # Note: Change n to the number of unique patterns at the end
        # Note: Randomize timing later since you do it when you merge

        # What this function returns (or void) is therefore undecided because I don't know how you want to implement the mergeWaves 
        # with the randomization of timings
        # 4 Options:
        # 1. Do it all in this function, including the actual outputting into the LEDs
        # 2. Output the log and randomize the timings and output it in another function
        # 3: Output the log and randomize it in the running while loop
        # 4: Or do some combination of them, or something that I didn't think of.

        # Just FYI: The main idea of this function is to run it once every iteration in the running while loop (which runs forever)
        # and have it continiously output patterns, only to be interrupted using if statements when:
            # 1. Ultrasonics sense something and it goes into the hand tracking ripple/circularWave
            # 2. When the time isn't when people will be using it; eg: at night, where it will be turned off.



"""
For images

Note: The images have to be the same or smaller width and height as the board
"""
def displayImage(image_path, blend = False, lock_aspect = False):
    image = Image.open(image_path)
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
def randomiseImage(delay = 0):
    # Get all the image paths in the images directory
    image_dir = "images/"
    all_images = [f"{image_dir}{im}" for im in os.listdir(image_dir)]

    # Have an empty array to store all the random numbers chosen
    chosen_numbers = []

    total_shown = 0
    while total_shown < len(all_images):
        number = random.randint(0, len(all_images) - 1)
        # If it's not already chosen
        if number not in chosen_numbers:
            displayImage(all_images[number], lock_aspect=True)
            chosen_numbers.append(number)
            time.sleep(delay)

            total_shown += 1


"""
Other functions
"""
def ultrasonicSensors(x, y):
    # Store the previous x and y values
    p_x, p_y = x, y

    # Get data from the sensors
    s1 = sensor1.distance
    s2 = sensor2.distance
    s3 = sensor3.distance
    s4 = sensor4.distance

    # Check if the sensors detected anything
    if s1 != 1 and (s2 != 1 or s3 != 1 or s4 != 1):
        # Get the x and y value of the detected object from the multiple sensors
        if s2 > 0.7:
            s2 = 1
        if s3 > 0.7:
            s3 = 1
        if s4 > 0.7:
            s4 = 1

        if s2 < s3 and s2 < s4:
            y = s2
        elif s3 < s2 and s3 < s4:
            y = s3
        else:
            y = s4

        x = s1
        y = 1 - y

        # Weird bug but the sensor data only stores in the variable if you print it out
        print(x, y)

        # Calculate change in previous and current value
        if p_x != -1 and p_y != -1:
            dx = math.fabs(x - p_x)
            dy = math.fabs(y - p_y)
        else:
            dx, dy = 0, 0
            x = 0
            y = 0

        # Map the physical positions to the LED positions
        l_x = int(round(round(x, 4) * 26, 0))
        l_y = int(round(round(y, 4) * 20, 0))

        # Compensate for sensing inaccuracies
        if l_y != 0:
            if l_y < 11:
                l_y -= 3
            elif l_y < 16:
                l_y -= 2

        if s1 < 1 and (s2 < 1 or s3 < 1 or s4 < 1) and dx < MAX_CHANGE and dy < MAX_CHANGE:
            displayWave(precomputeColours(precomputeRipple(l_x, l_y, 5), COLOURS["Green"], COLOURS["Black"], 3))
        elif p_x != 0 and p_y != 0:
            displayWave(precomputeColours(precomputeRipple(l_x, l_y, 5), COLOURS["Green"], COLOURS["Black"], 3))
        else:
            displayWave(precomputeColours(precomputeRipple(l_x, l_y, 5), COLOURS["Green"], COLOURS["Black"], 3))
    else:
        x, y = 0, 0

    return x, y

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

"""
Main loop
"""
# Reset board
setAllPixelsColour(pixels, COLOURS["Black"])

# Compute test waves
# merge1 = []
# merge1.append(precomputeColours(precomputeRain(10), COLOURS["Dark Blue"], COLOURS["Black"], 7))
# merge1.append(precomputeColours(precomputeRain(11), COLOURS["Dark Blue"], COLOURS["Black"], 7))
# merge1.append(precomputeColours(precomputeRain(16), COLOURS["Dark Blue"], COLOURS["Black"], 7))
# merge1.append(precomputeColours(precomputeRain(5), COLOURS["Dark Blue"], COLOURS["Black"], 7))
# merge1.append(precomputeColours(precomputeRain(23), COLOURS["Dark Blue"], COLOURS["Black"], 7))
# merge1.append(precomputeColours(precomputeRain(1), COLOURS["Dark Blue"], COLOURS["Black"], 7))
# merge1.append(precomputeColours(precomputeRain(29), COLOURS["Dark Blue"], COLOURS["Black"], 7))
# merged1 = mergeWaves(merge1, [0, 3, 4, 10, 2, 7, 0])
# 
# merge2 = []
# merge2.append(precomputeColours(precomputeCircularWave(15, 10, 9), COLOURS["Red"], COLOURS["Black"], 3))
# merge2.append(precomputeColours(precomputeWave(1, 29), COLOURS["Red Orange"], COLOURS["Black"], 6))
# merge2.append(precomputeColours(precomputeRipple(10, 6, 10), COLOURS["Lime"], COLOURS["Black"], 4))
# merged2 = mergeWaves(merge2, [5, 0, 7])

# Main running loop
x, y = -1, -1
while True:
#     setAllPixelsColour(pixels, COLOURS["Black"])
#     pixels, pixel_framebuf = changeBrightness(1)
#     displayWave(merged1, 0.05)
# 
#     setAllPixelsColour(pixels, COLOURS["Black"])
# #     pixels, pixel_framebuf = changeBrightness(0.3)
#     displayWave(merged2, 0.08)
# 
#     setAllPixelsColour(pixels, COLOURS["Black"])
#     drawText("CLASS", COLOURS["Dark Blue"], 0, 2)
#     drawText("2023", COLOURS["Purple"], 4, 11)
#     time.sleep(5)
# 
#     setAllPixelsColour(pixels, COLOURS["Black"])
#     drawText("LED", COLOURS["Lime"], 7, 2)
#     drawText("WALL", COLOURS["Yellow"], 4, 11)
#     time.sleep(5)


    # To use ultrasonic sensors
    # Store the previous x and y values
    p_x, p_y = x, y
    print(x, y)

    # Get data from the sensors
    s1 = sensor1.distance
    s2 = sensor2.distance
    s3 = sensor3.distance
    s4 = sensor4.distance

    # Check if the sensors detected anything
    if s1 != 1 and (s2 != 1 or s3 != 1 or s4 != 1):
        # Get the x and y value of the detected object from the multiple sensors
        if s2 > 0.7:
            s2 = 1
        if s3 > 0.7:
            s3 = 1
        if s4 > 0.7:
            s4 = 1

        if s2 < s3 and s2 < s4:
            y = s2
        elif s3 < s2 and s3 < s4:
            y = s3
        else:
            y = s4

        x = s1
        y = 1 - y

        # Weird bug but the sensor data only stores in the variable if you print it out
        print(x, y)

        # Calculate change in previous and current value
        if p_x != -1 and p_y != -1:
            dx = math.fabs(x - p_x)
            dy = math.fabs(y - p_y)
        else:
            dx, dy = 0, 0
            x = 0
            y = 0

        # Map the physical positions to the LED positions
        l_x = int(round(round(x, 4) * 26, 0))
        l_y = int(round(round(y, 4) * 20, 0))

        # Compensate for sensing inaccuracies
        if l_y != 0:
            print(l_x, l_y)
            if l_y < 11:
                l_y -= 3
            elif l_y < 16:
                l_y -= 2

        if s1 < 1 and (s2 < 1 or s3 < 1 or s4 < 1) and dx < MAX_CHANGE and dy < MAX_CHANGE:
            displayWave(precomputeColours(precomputeRipple(l_x, l_y, 5), COLOURS["Green"], COLOURS["Black"], 3))
        elif p_x != 0 and p_y != 0:
            displayWave(precomputeColours(precomputeRipple(l_x, l_y, 5), COLOURS["Green"], COLOURS["Black"], 3))
        else:
            displayWave(precomputeColours(precomputeRipple(l_x, l_y, 5), COLOURS["Green"], COLOURS["Black"], 3))
    else:
        x, y = -1, -1
