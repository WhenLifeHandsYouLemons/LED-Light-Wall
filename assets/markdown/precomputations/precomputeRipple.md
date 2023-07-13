# precomputeRipple function

## Overview

The `precomputeRipple` function computes an array of LED coordinates for each tick of a wave, given the starting LED coordinates and the duration of the wave. The function uses a simple algorithm to calculate the coordinates of each LED that should be illuminated for each tick of the wave. The resulting array can be used to display the wave on an LED display.

## Function Signature

```py
def precomputeRipple(x: int,
                     y: int,
                     duration: int) -> List[List[List[int, int]]]:
    pass
```

## Parameters

- `x` = `(int)`: An integer representing the x-coordinate of the starting LED.

- `y` = `(int)`: An integer representing the y-coordinate of the starting LED.

- `duration` = `(int)`: An integer representing the duration of the wave in ticks.

## Return Value

- `List[List[List[int, int]]]`: A three-dimensional list representing the LED coordinates for each tick of the wave. Each top-level item in the list represents a tick of the wave, and each item in the second-level list represents an LED that should be illuminated for that tick. The third-level list contains the x and y coordinates of the LED.

## Function Description

The `precomputeRipple` function computes anarray of LED coordinates for each tick of a wave, given the starting LED coordinates and the duration of the wave. The function first creates an empty list called `precomputed_wave` to store the LED coordinates for each tick of the wave.

The function then adds the starting LED coordinates to the first item of `precomputed_wave`, representing the first tick of the wave.

For each subsequent tick of the wave, the function loops through the LED coordinates for the previous tick and calculates the coordinates of each LED that should be illuminated for the next tick. The function stores these coordinates in a new list called `tick_array`, and adds `tick_array` to `precomputed_wave`.

The function uses the `used_leds` list to keep track of which LEDs have already been included in previous ticks, to avoid duplicates. The function checks the LED to the left, right, above, and below each LED in the previous tick, and adds any new LEDs to `tick_array` if they meet the criteria. The function then adds these new LEDs to `used_leds` to avoid duplicates.

The function returns the `precomputed_wave` list, which contains the LED coordinates for each tick of the wave.

## Example Usage

```py
# Compute precomputed_wave for a wave starting at LED (0, 0) with a duration of 5 ticks
precomputed_wave = precomputeRipple(0, 0, 5)
```

In the example above, we call the`precomputeRipple` function to compute an array of LED coordinates for a wave starting at LED $(0, 0)$ with a duration of 5 ticks.

## Exceptions

- The `precomputeRipple` function assumes that the LED display is represented as a rectangular grid of LEDs with a width of `board_width` and a height of `board_height`. If the LED display is represented differently, the `precomputeRipple` function should be modified accordingly.

- The `precomputeRipple` function assumes that the `board_width` and `board_height` constants are defined properly. If these constants are not defined properly, the `precomputeRipple` function may not work as expected.

- The `precomputeRipple` function assumes that the `setPixelColour` function is defined properly and that it can set the color of a single LED on the LED display. If the `setPixelColour` function is not defined properly or if the LED display is represented differently, the `precomputeRipple` function should be modified accordingly.

- The `precomputeRipple` function may be computationally expensive for durations of over 60 ticks, as noted in the function's comments. If the duration of the wave is expected to be longer than 60 ticks, the function may need to be optimized or replaced with a more efficient algorithm.

- The coordinate system starts from the bottom left and the first LED is at position $(0, 0)$.