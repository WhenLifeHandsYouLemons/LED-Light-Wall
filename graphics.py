"""
For graphics

Note: The coordinates start from the top left and the first LED is (0, 0)
"""
import time
import math
import random

# Custom imports
from rpi import *
from utilities import *
from precomputations import *
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

# Displays multiple wave patterns with random colours, positions, durations, and more
def randomisePatterns():
    N = 6   # Number of patterns available
    NUM_PATTERNS = random.randint(1, 3)

    print(f"Total patterns: {NUM_PATTERNS}")

    MIN_FADE = 3
    MAX_FADE = 7

    MIN_RIPPLE_DURATION = 5
    MAX_DURATION = 30
    if NUM_PATTERNS == 3:
        MAX_DURATION = 20

    MAX_TIME = 10

    MIN_SEPARATION = 2

    # Log to contain all instances of waves to merge at the end
    log = []

    # Log of position of ripples/circular waves so they don't overly overlap
    pos = []

    # Cycle through color wheel for complementary colors
    color = random.randint(0, len(COLOURS) - 5)

    for i in range(NUM_PATTERNS):
        pattern = random.randint(1, N**2)
        # Making it rarer that an image or text is chosen
        if pattern != 36:
            pattern = pattern % 5
            pattern += 1

        print(f"Getting pattern {i+1}, chosen {pattern}")

        if pattern == 1:    # Wave
            direction = random.randint(0, 3)
            if direction in [0, 2]:
                duration = random.randint(10, BOARD_HEIGHT - 1)
            else:
                duration = random.randint(15, BOARD_WIDTH - 1)
            wave = precomputeWave(direction, duration)

            # Randomize color
            # d = dice to have chance of outlying colors of brown, grey, black and white
            d_max = 15
            d = random.randint(0, d_max)

            if d == d_max:
                i_color = len(COLOURS) - 1
            elif d == d_max - 2:
                i_color = len(COLOURS) - 3
            else:
                i_color = color

                if d == 2 or d == 3: # To skip some colors, for variance
                    color += d
                else:
                    color += 1

                # Reset back to 0
                if color > len(COLOURS) - 5:
                    color = 0 + (color - (len(COLOURS) - 5))

            # Set ending color to always be black
            e_color = len(COLOURS) - 2

            fade = random.randint(MIN_FADE, MAX_FADE)

            wave = precomputeColours(wave, COLOURS[num_to_colours[i_color]], COLOURS[num_to_colours[e_color]], fade)
            log.append(wave)
        elif pattern == 2:  # Ripple
            # Randomize duration
            duration = random.randint(MIN_RIPPLE_DURATION, MAX_DURATION)

            # Randomize position
            x = random.randint(0, 29)
            y = random.randint(0, 19)

            # Check that positioning of the origin is 'Unique'- the difference in positioning must be greater than 4 LEDs
            check = False
            for ii in pos:
                dx = math.fabs(x - ii[0])
                dy = math.fabs(y - ii[1])

                if (dx < MIN_SEPARATION or dy < MIN_SEPARATION):
                    check = True

            while check:
                x = random.randint(0, 29)
                y = random.randint(0, 19)

                check = False

                for ii in pos:
                    dx = math.fabs(x - ii[0])
                    dy = math.fabs(y - ii[1])

                    if (dx < MIN_SEPARATION or dy < MIN_SEPARATION):
                        check = True

            wave = precomputeRipple(x, y, duration)
            pos.append([x, y])

            # Randomize color
            # d = dice to have chance of outlying colors of brown, grey, black and white
            d_max = 15
            d = random.randint(0, d_max)
            if d == d_max:
                i_color = len(COLOURS) - 1
            elif d == d_max - 2:
                i_color = len(COLOURS) - 3
            else:
                i_color = color

                if d == 2 or d == 3: # To skip some colors, for variance
                    color += d
                else:
                    color += 1

                # Reset back to 0
                if color > len(COLOURS) - 5:
                    color = 0 + (color - (len(COLOURS) - 5))

            # Set ending color to always be black
            e_color = len(COLOURS) - 2

            fade = random.randint(MIN_FADE, MAX_FADE)

            wave = precomputeColours(wave, COLOURS[num_to_colours[i_color]], COLOURS[num_to_colours[e_color]], fade)
            log.append(wave)
        elif pattern == 3:  # Rain
            num_of_drops = random.randint(5, 10)
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
                if color > len(COLOURS) - 5:
                    color = 0 + (color - (len(COLOURS) - 5))

            # Set ending color to always be black
            e_color = len(COLOURS) - 2

            temp_pos = []

            for ii in range(num_of_drops):
                # Ensure that the same x position doesn't repeat
                check = False
                while check == False:
                    check = True
                    x = random.randint(0, 29)

                    for iii in temp_pos:
                        if iii == x:
                            check = False

                fade = random.randint(MIN_FADE, MAX_FADE)
                wave = precomputeRain(x)
                wave = precomputeColours(wave, COLOURS[num_to_colours[i_color]], COLOURS[num_to_colours[e_color]], fade)

                temp_pos.append(x)
                log.append(wave)
        elif pattern == 4:  # Lines
            # Randomize width of line
            width = random.randint(1, 3)

            # Randomize start of line
            x = random.randint(0, 29)
            y = random.randint(0, 19)

            # Check that positioning of the origin is 'Unique'- the difference in positioning must be greater than 4 LEDs
            check = False
            for ii in pos:
                dx = math.fabs(x - ii[0])
                dy = math.fabs(y - ii[1])

                if (dx < MIN_SEPARATION or dy < MIN_SEPARATION):
                    check = True

            while check:
                x = random.randint(0, 29)
                y = random.randint(0, 19)
                check = False

                for ii in pos:
                    dx = math.fabs(x - ii[0])
                    dy = math.fabs(y - ii[1])

                    if (dx < MIN_SEPARATION or dy < MIN_SEPARATION):
                        check = True

            e_check = True
            while e_check:
                # Randomize end of line
                e_x = random.randint(0, 29)
                e_y = random.randint(0, 19)
                e_check = False

                # Check that positioning of the origin is 'Unique'- the difference in positioning must be greater than 4 LEDs
                check = False
                for ii in pos:
                    dx = math.fabs(e_x - ii[0])
                    dy = math.fabs(e_y - ii[1])

                    if (dx < MIN_SEPARATION or dy < MIN_SEPARATION):
                        check = True

                while check:
                    e_x = random.randint(0, 29)
                    e_y = random.randint(0, 19)
                    check = False

                    for ii in pos:
                        dx = math.fabs(e_x - ii[0])
                        dy = math.fabs(e_y - ii[1])

                        if (dx < MIN_SEPARATION or dy < MIN_SEPARATION):
                            check = True

                d_max = 15
                d = random.randint(0, d_max)
                if d == d_max:
                    i_color = len(COLOURS) - 1
                elif d == d_max - 2:
                    i_color = len(COLOURS) - 3
                else:
                    i_color = color

                    if d == 2 or d == 3: # To skip some colors, for variance
                        color += d
                    else:
                        color += 1

                    # Reset back to 0
                    if color > len(COLOURS) - 5:
                        color = 0 + (color - (len(COLOURS) - 5))

                # Set ending color to always be black
                e_color = len(COLOURS) - 2

                wave = precomputeLines(x, y, e_x, e_y, width)

                # Fixes ZeroDivisionError in precomputeColours
                if len(wave) == 1:
                    e_check = True

            fade = random.randint(MIN_FADE, MAX_FADE)
            wave = precomputeColours(wave, COLOURS[num_to_colours[i_color]], COLOURS[num_to_colours[e_color]], fade)

            pos.append([x, y])
            pos.append([e_x, e_y])
            log.append(wave)
        elif pattern == 5:  # Circle
            # Randomize duration
            duration = random.randint(MIN_RIPPLE_DURATION, MAX_DURATION)

            # Randomize position
            x = random.randint(0, 29)
            y = random.randint(0, 19)

            # Check that positioning of the origin is 'unique'- the difference in positions must be greater than 4 LEDs
            check = False
            for ii in pos:
                dx = math.fabs(x - ii[0])
                dy = math.fabs(y - ii[1])

                if (dx < MIN_SEPARATION or dy < MIN_SEPARATION):
                    check = True

            while check:
                x = random.randint(0, 29)
                y = random.randint(0, 19)
                check = False

                for ii in pos:
                    dx = math.fabs(x - ii[0])
                    dy = math.fabs(y - ii[1])

                    if (dx < MIN_SEPARATION or dy < MIN_SEPARATION):
                        check = True

            wave = precomputeCircularWave(x, y, duration)
            pos.append([x, y])

            # Randomize color
            # d = dice to have chance of outlying colors of brown, grey, black and white
            d_max = 15
            d = random.randint(0, d_max)
            if d == d_max:
                i_color = len(COLOURS) - 1
            elif d == d_max - 2:
                i_color = len(COLOURS) - 3
            else:
                i_color = color

                if d == 2 or d == 3: # To skip some colors, for variance
                    color += d
                else:
                    color += 1

                # Reset back to 0
                if color > len(COLOURS) - 5:
                    color = 0 + (color - (len(COLOURS) - 5))

            # Set ending color to always be black
            e_color = len(COLOURS) - 2

            fade = random.randint(MIN_FADE, MAX_FADE)

            wave = precomputeColours(wave, COLOURS[num_to_colours[i_color]], COLOURS[num_to_colours[e_color]], fade)
            log.append(wave)
        elif pattern == 36:  # Text or image
            # Choose between text or image
            pat_type = random.randint(0, 1)

            # Text
            if pat_type == 0:
                log.append("text")
            # Image
            else:
                log.append("image")

        print(f"Got pattern {i+1}")

    # Go through log and either add to a to-merge array or if we need to display text and images (non-merge array)
    to_merge = []
    non_merge = []
    for item in log:
        if type(item) == str:
            non_merge.append(item)
        else:
            to_merge.append(item)

    # Randomise all the pattern timings
    TIMINGS = [random.randint(0, MAX_TIME) for item in to_merge]

    print("Merging waves...")

    # Merge all to_merge patterns
    merged_patterns = mergeWaves(to_merge, TIMINGS)

    return merged_patterns, non_merge

# This takes a precomputed array and a text/image array and displays it on the board
def displayRandomPatterns(pixel_framebuf, merged_array, non_merged_array):
    displayWave(merged_array, 0.05)

    # Used for not showing the same image again
    invalid_nums = []

    for item in non_merged_array:
        if item == "image":
            num = randomiseImage(pixel_framebuf, invalid_nums, 1)
            invalid_nums.append(num)
        elif item == "text":
            # Get random colour
            colour_val = random.randint(0, len(num_to_colours) - 1)

            randomiseText(pixel_framebuf, num_to_colours[colour_val])
