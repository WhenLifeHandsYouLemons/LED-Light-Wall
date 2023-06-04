# Imports
import time
import sys
import pygame
import copy

board_width = 30
board_height = 20
pixel_brightness = 1


"""
Utilities
"""
mapping = {}
# Function to create the 2D array and map each pixel
def createGrid(x, y):
    n = 0
    i = y - 1
    right_direction = True
    array = [[None for i in range(x)] for j in range(y)]

    val = board_width * board_height
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
map_grid = createGrid(board_width, board_height)

# Getting the number of the LED when you enter X and Y coordinates
def getLED(input_x, input_y):
    if input_x < 0 or input_y < 0 or input_x > board_width or input_y > board_height:
        return (board_height * board_width) + 1

    right_direction = True
    output = input_y * board_width

    if input_y % 2 != 0:
        right_direction = False

    if right_direction:
        output += input_x
    else:
        output += ((board_width - 1) - input_x)

    return output + 1

# Set all pixels to a specified colour
def setAllPixelsColour(colour):
    # Go through the total y LEDs
    for y in range(board_height+1):
        # Go through the total x LEDs
        for x in range(board_width):
            # drawLED at x, y and the colour
            drawLED(x, y, colour)

    pygame.display.update()

# Set specified colour to consecutive or single pixels
def setPixelsColour(colour, pixel_index_start, pixel_index_end=None):
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
colours = {
    "Red" : (255, 0, 0),
    "Pink" : (100, 75, 80),
    "Vermilion" : (89, 26, 20),
    "Orange" : (255, 165, 0),
    "Amber" : (100, 75, 0),
    "Yellow" : (255, 255, 0),
    "Lime": (75, 100, 0),
    "Green" : (0, 255, 0),
    "Dark Green" : (0, 20, 13),
    "Light Blue" : (68, 85, 90),
    "Blue" : (0, 0, 255),
    "Dark Blue" : (0, 0, 55),
    "Purple" : (160, 32, 240),
    "Grey" : (128, 128, 128),
    "Brown" : (139, 69, 19),
    "Black" : (0, 0, 0),
    "White" : (255, 255, 255)
}

# Startup function (To check there is no errors with the code)
def startup(delay):
    for key in iter(colours):
        setAllPixelsColour(colours[key])
        time.sleep(delay)


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
    #   1 = Right to left
    #   2 = Down to up
    #   3 = Left to right
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
# The wave_array has to be a 4d array (include colour information too)
def displayWave(wave_array, delay):
    for tick in wave_array:
        for LED in tick:
            setPixelsColour(LED[2], getLED(LED[0], LED[1]))

        pygame.display.update()
        time.sleep(delay)


"""
For Pygame
"""
# Variables for Pygame
pixel_size = 20
gap_size = 5

# Pygame window stuff
bg_colour = 0, 0, 0
window_height = (pixel_size + gap_size) * board_height
window_width = (pixel_size + gap_size) * board_width
WIN = pygame.display.set_mode((window_width, window_height))
WIN.fill(bg_colour)

def drawLED(x, y, colour):
    corrected_x = (x * (pixel_size + gap_size))
    corrected_y = window_height - (y * (pixel_size + gap_size)) - (pixel_size + gap_size)
    pygame.draw.rect(WIN, (colour[0], colour[1], colour[2]), pygame.Rect(corrected_x, corrected_y, pixel_size, pixel_size))

# Set FPS for pygame
clock = pygame.time.Clock()

# Main loop
RUNNING_WINDOW = True

# Reset board
setAllPixelsColour(colours["Black"])

# Compute test waves
to_merge = []
test_1 = precomputeRipple(25, 14, 10)
test_1_c = precomputeColours(test_1, colours["Green"], colours["Red"], 3)
to_merge.append(test_1_c)
test_2 = precomputeWave(0, 15)
test_2_c = precomputeColours(test_2, colours["Blue"], colours["Black"], 7)
to_merge.append(test_2_c)
test_3 = precomputeRipple(10, 8, 20)
test_3_c = precomputeColours(test_3, colours["Light Blue"], colours["Pink"], 7)
to_merge.append(test_3_c)
merged_test_waves = mergeWaves(to_merge)

while RUNNING_WINDOW == True:
    clock.tick(30)

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pos()

    setAllPixelsColour(colours["Black"])
    displayWave(merged_test_waves, 0.3)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False
            pygame.quit()

sys.exit()
