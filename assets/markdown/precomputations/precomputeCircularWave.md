# precomputeCircularWave function

## Overview

The `precomputeCircularWave` function computes an array of LED coordinates for each tick of a circular wave, given the starting LED coordinates and the duration of the wave. The function uses the Bresenham Circle Algorithm to calculate the coordinates of the LEDs that should be illuminated for each tick of the wave. The resulting array can be used to display the wave on an LED display.

## Function Signature

```py
def precomputeCircularWave(x: int,
                           y: int,
                           duration: int) -> List[List[List[int, int]]]:
    pass
```

## Parameters

- `x` = `(int)`: An integer representing the x-coordinate of the center of the circular wave.

- `y` = `(int)`: An integer representing the y-coordinate of the center of the circular wave.

- `duration` = `(int)`: An integer representing the duration of the wave in ticks.

## Return Value

- `List[List[List[int, int]]]`: A three-dimensional list representing the LED coordinates for each tick of the wave. Each top-level item in the list represents a tick of the wave, and each item in the second-level list represents an LED that should be illuminated for that tick. The third-level list contains the x and y coordinates of the LED.

## Function Description

The `precomputeCircularWave` function computes an array of LED coordinates for each tick of a circular wave, given the starting LED coordinates and the duration of the wave. The function first creates an empty list called `precomputed_wave` to store the LED coordinates for each tick of the wave.

The function then hard-codes the first tick of the wave by adding the starting LED coordinates to the first item of `precomputed_wave`.

For each subsequent tick of the wave, the function uses the Bresenham Circle Algorithm to calculate the coordinates of the LEDs that should be illuminated. The algorithm computes the coordinates of the LEDs in the first octant of the circle and then mirrors these coordinates in the other octants.

The function then adds the mirrored coordinates to the `tick_array` list. The `offset_x` and `offset_y` variables are used to adjust the coordinates of the LEDs to the correct position relative to the center of the circle.

The function then removes any duplicate LEDs from the `tick_array` list. This is done to avoid illuminating the same LED multiple times in the same tick.

Finally, the `tick_array` is added to the `precomputed_wave` list, and the function returns the `precomputed_wave` list.

## Example Usage

```py
# Compute precomputed_wave for a circular wave centered at LED (0, 0) with a duration of 5 ticks
precomputed_wave = precomputeCircularWave(0, 0, 5)
```

In the example above, we call the `precomputeCircularWave` function to compute an array of LED coordinates for a circular wave centered at LED $(0, 0)$ with a duration of 5 ticks.

## Exceptions

- The `precomputeCircularWave` function assumes that the LED display is represented as a rectangular grid of LEDs with a width of `board_width` and a height of `board_height`. If the LED display is represented differently, the `precomputeCircularWave` function should be modified accordingly.

- The `precomputeCircularWave` function assumes that the `board_width` and `board_height` constants are defined properly. If these constants are not defined properly, the `precomputeCircularWave` function may not work as expected.

- The `precomputeCircularWave` function assumes that the `setPixelColour` function is defined properly and that it can set the color of a single LED on the LED display. If the `setPixelColour` function is not defined properly or if the LED display is represented differently, the `precomputeCircularWave` function should be modified accordingly.

- The `precomputeCircularWave` function may be computationally expensive for durations of over 60 ticks, as noted in the function's comments. If the duration of the wave is expected to be longer than 60 ticks, the function may need to be optimized or replaced with a more efficient algorithm.

- The coordinate system starts from the bottom left and the first LED is at position $(0, 0)$.