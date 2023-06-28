"""
For precomputation of graphics

Note: The coordinates start from the bottom left and the first LED is (0, 0)
"""
import time
import math
import copy

# Custom imports
from rpi import *
from utilities import *
from ultrasonics import checkUltrasonics

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
            led1 = [offset_x + LED[0], offset_y + LED[1]]
            if led1[0] < BOARD_WIDTH and led1[0] >= 0 and led1[1] < BOARD_HEIGHT and led1[1] >= 0:
                tick_array.append(led1)

            led2 = [offset_x - LED[0], offset_y + LED[1]]
            if led2[0] < BOARD_WIDTH and led2[0] >= 0 and led2[1] < BOARD_HEIGHT and led2[1] >= 0:
                tick_array.append(led2)

            led3 = [offset_x + LED[0], offset_y - LED[1]]
            if led3[0] < BOARD_WIDTH and led3[0] >= 0 and led3[1] < BOARD_HEIGHT and led3[1] >= 0:
                tick_array.append(led3)

            led4 = [offset_x - LED[0], offset_y - LED[1]]
            if led4[0] < BOARD_WIDTH and led4[0] >= 0 and led4[1] < BOARD_HEIGHT and led4[1] >= 0:
                tick_array.append(led4)

            led5 = [offset_x + LED[1], offset_y + LED[0]]
            if led5[0] < BOARD_WIDTH and led5[0] >= 0 and led5[1] < BOARD_HEIGHT and led5[1] >= 0:
                tick_array.append(led5)

            led6 = [offset_x - LED[1], offset_y + LED[0]]
            if led6[0] < BOARD_WIDTH and led6[0] >= 0 and led6[1] < BOARD_HEIGHT and led6[1] >= 0:
                tick_array.append(led6)

            led7 = [offset_x + LED[1], offset_y - LED[0]]
            if led7[0] < BOARD_WIDTH and led7[0] >= 0 and led7[1] < BOARD_HEIGHT and led7[1] >= 0:
                tick_array.append(led7)

            led8 = [offset_x - LED[1], offset_y - LED[0]]
            if led8[0] < BOARD_WIDTH and led8[0] >= 0 and led8[1] < BOARD_HEIGHT and led8[1] >= 0:
                tick_array.append(led8)

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
            for i in range(1, fade+1):
                if (tick_count - i) < 0:
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
            setPixelsColour(pixels, LED[2], getLED(LED[0], LED[1]))

        pixels.show()
        checkUltrasonics()
        time.sleep(delay)
