# Imports
import time
# To use these, follow this guide: https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage
import board, neopixel
import copy
# To use these, follow this guide: https://learn.adafruit.com/easy-neopixel-graphics-with-the-circuitpython-pixel-framebuf-library/import-and-setup
from adafruit_pixel_framebuf import PixelFramebuffer
from PIL import Image
import random


"""
Initialisation
"""
# Variables for initialising NeoPixels
pixel_pin = board.D18
board_width = 30
board_height = 20
pixel_brightness = 0.5

# Initialise NeoPixel grid
pixels = neopixel.NeoPixel(
    pixel_pin,
    board_width * board_height,
    brightness=pixel_brightness,    # Brightness out of 1
    auto_write=False,
    pixel_order=neopixel.GRB
)

# Initialise framebuffer for displaying graphics easily
pixel_framebuf = PixelFramebuffer(
    pixels,
    board_width,
    board_height,
    rotation=2,
    reverse_x=True,
    reverse_y=False
)


"""
Useful functions
"""
# Getting the number of the LED when you enter X and Y coordinates
def getLED(input_x, input_y):
    right_direction = True
    output = input_y * board_width
    if input_y % 2 != 0:
        right_direction = False
    if right_direction:
        output += input_x
    else:
        output += ((board_width - 1) - input_x)
    return output + 0   # This is because the LEDs start at 1 not 0

def RGBToHex(colour):
    return int("{:02x}{:02x}{:02x}".format(colour[0], colour[1], colour[2]), 16)

# Set all pixels to a specified colour
def setAllPixelsColour(colour):
#     pixels.fill(colour)
#     pixels.show()
    pixel_framebuf.fill(RGBToHex(colour))
    pixel_framebuf.display()

# Set specified colour to consecutive or single pixels
def setPixelsColour(colour, pixel_index_start, pixel_index_end=None):
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

# Dictionary for words
colours = {
    "Red" : (255, 0, 0),
    "Orange" : (255, 165, 0),
    "Yellow" : (255, 255, 0),
    "Green" : (0, 255, 0),
    "Blue" : (0, 0, 255),
    "Purple" : (160, 32, 240),
    "Black" : (0, 0, 0),
    "White" : (255, 255, 255)
}

# Startup function (To check there is no errors with the code)
def startup():
    setAllPixelsColour(colours["Red"])
    time.sleep(1)
    setAllPixelsColour(colours["Orange"])
    time.sleep(1)
    setAllPixelsColour(colours["Yellow"])
    time.sleep(1)
    setAllPixelsColour(colours["Green"])
    time.sleep(1)
    setAllPixelsColour(colours["Blue"])
    time.sleep(1)
    setAllPixelsColour(colours["Purple"])
    time.sleep(1)


"""
For waves

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
            if [i_x + 1, i_y] not in used_leds and i_x + 1 < board_width:
                # Add it to tick_array
                tick_array.append([i_x + 1, i_y])
                # Add to used_leds
                used_leds.append([i_x + 1, i_y])
                # If not, then add that to the tick_array

            # Check if the LED above it is in any of the previous arrays
            if [i_x, i_y + 1] not in used_leds and i_y + 1 < board_height:
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

# Output should be in the same format of precomputeRipple so that precomputeColours can be used on this
def precomputeWave(pos, duration):
    # Pos:
    #   0 = Up to down
    #   1 = Down to up
    #   2 = Right to left
    #   3 = Left to right
    precomputed_wave = [[]]
    if pos == 0:
        x = 0
        while x < 30:
            precomputed_wave[0].append([x, 19])
            x += 1
    elif pos == 1:
        x = 0
        while x < 30:
            precomputed_wave[0].append([x, 0])
            x += 1
    elif pos == 2:
        y = 0
        while y < 20:
            precomputed_wave[0].append([29, y])
            y += 1
    elif pos == 3:
        y = 0
        while y < 20:
            precomputed_wave[0].append([0, y])
            y += 1

    for tick in range(1, duration):
        tick_array = []
        # Get the previous tick array to calculate next tick
        previous_tick_array = precomputed_wave[tick-1]

        # For every LED in the previous tick array
        for i in previous_tick_array:
            # Get the separate x and y values to change it
            i_x = i[0]
            i_y = i[1]

            if pos == 0:
                tick_array.append([i_x, i_y - 1])
            elif pos == 1:
                tick_array.append([i_x, i_y + 1])
            elif pos == 2:
                tick_array.append([i_x - 1, i_y])
            elif pos == 3:
                tick_array.append([i_x + 1, i_y])
        # Add tick_array to precomputed_wave
        precomputed_wave.append(tick_array)

    return precomputed_wave




# Precompute and extend the precompute array into 4D crest colors and fade colors
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

    # # Add all previous tick's LEDs without changing colour to have accurate colour mixing
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
def mergeWaves(wave_arrays):
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

    # Merge all duplicates in each tick separately
    merged_wave_array = []
    used_coords = []
    tick = 0
    while tick < len(sorted_wave_array):
        # Get the current led coords
        current_led_no = 0
        temp_tick = []
        used_coords = []

        while current_led_no < len(sorted_wave_array[tick]):
            if [sorted_wave_array[tick][current_led_no][0], sorted_wave_array[tick][current_led_no][1]] not in used_coords:
                # Go through all the coords in the current tick
                check_led_no = current_led_no + 1
                total_leds = 1
                total_colour = sorted_wave_array[tick][current_led_no][2].copy()
                used_coords.append([sorted_wave_array[tick][current_led_no][0], sorted_wave_array[tick][current_led_no][1]])

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

# This takes a wave array (can be merged or just a single wave array)
def displayWave(wave_array):
    for tick in wave_array:
        for LED in tick:
            setPixelsColour(LED[2], getLED(LED[0], LED[1]))

        pixels.show()
        time.sleep(0.3)


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
def drawText(text, x, y, colour):
    pixel_framebuf.text(text, x, y, RGBToHex(colour))
    pixel_framebuf.display()

# Animate text scrolling from right to left
# Note: The text will always start from off-screen to the right and go to the left
def scrollText(end_x, y, text, colour, wait_time):
    x = board_width + 1
    while x > end_x:
        drawText(text, x, y, colour)
        time.sleep(wait_time)
        setAllPixelsColour(colours["Black"])
        x -= 1
        
        
def random_pattern():
    n = 5 # n = number of unique patterns
    num_of_patterns = random.randint(1, 3)
    if num_of_patterns == 3:
        max = 7
    i = 0
    while i < num_of_patterns:
        pattern = random.randint(1, n)
        if pattern == 1:
            # Call function
        elif pattern == 2:
            # Call function
        elif pattern == 3:
            # Call function
        elif pattern == 4:
            # Call function
        elif pattern == 5:
            # Call function
    
    


"""
For images

Note: The images have to be the same width and height as the board
"""
def displayImage(image_path, blend=False):
    image = Image.open(image_path)

    if blend:
        background = Image.new("RGBA", (board_width, board_height))
        background.alpha_composite(image)
        pixel_framebuf.image(background.convert("RGB"))
    else:
        pixel_framebuf.image(image.convert("RGB"))

    pixel_framebuf.display()


"""
Main loop
"""
# Reset board
setAllPixelsColour(colours["Black"])

# Compute test waves
to_merge = []
test_1 = precomputeRipple(25, 14, 5)
test_1_c = precomputeColours(test_1, colours["Green"], colours["Red"], 3)
to_merge.append(test_1_c)
test_2 = precomputeWave(2, 10)
test_2_c = precomputeColours(test_2, colours["Blue"], colours["Black"], 7)
to_merge.append(test_2_c)
# test_2_wave = precomputeRipple(10, 8, 20)
# test_2_wave_c = precomputeColours(test_2_wave, colours["Red"], colours["Orange"], 7)
# to_merge.append(test_2_wave_c)
merged_test_waves = mergeWaves(to_merge)

# Main running loop
while True:
    setAllPixelsColour(colours["Black"])
    print("Running")
    print("Still")
    time.sleep(0.5)
#     drawLine(0, 0, 3, 2, colours["Green"])
#     drawStraightLine(4, 4, 5, colours["Blue"], True)
#     drawStraightLine(4, 4, 4, colours["Blue"], False)
#     drawRect(6, 6, 8, 8, colours["Red"], False)
#     drawRect(8, 8, 3, 3, colours["Orange"], True)
#     drawCircle(10, 10, 1, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 2, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 3, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 4, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 5, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 6, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 7, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 8, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 9, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 10, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 11, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 12, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 13, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 14, colours["Green"])
#     time.sleep(0.5)
#     drawCircle(10, 10, 15, colours["Green"])
#     time.sleep(0.5)
#     drawText("XDD", 10, 10, colours["Red"])
#     time.sleep(1)
#     scrollText(-100, 5, "This is a test message", colours["Red"], 0.01)
    displayWave(merged_test_waves)
#     startup()
