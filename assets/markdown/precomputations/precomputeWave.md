# precomputeWave function

## Overview

The `precomputeWave` function computes an array of LED coordinates for a wave moving in a specified direction, given the starting position and the duration of the wave. The function outputs the LED coordinates in the same format as `precomputeRipple` so that `precomputeColours` can be used on the output.

## Function Signature

```py
def precomputeWave(pos: int,
                   duration: int) -> List[List[List[int, int]]]:
    pass
```

## Parameters

- `pos` = `(int)`: An integer representing the direction of the wave. The possible values of `pos` are:
  - 0 = Up to down
  - 1 = Right to left
  - 2 = Down to up
  - 3 = Left to right

- `duration` = `(int)`: An integer representing the duration of the wave in ticks.

## Return Value

- `List[List[List[int, int]]]`: A three-dimensional list representing the LED coordinates for each tick of the wave. Each top-level item in the list represents a tick of the wave, and each item in the second-level list represents an LED that should be illuminated for that tick. The third-level list contains the x and y coordinates of the LED.

## Function Description

The `precomputeWave` function computes an array of LED coordinates for a wave moving in a specified direction, given the starting position and the duration of the wave. The function first creates an empty list called `precomputed_wave` to store the LED coordinates for each tick of the wave.

The function then uses a series of conditional statements to determine the starting LED coordinates based on the direction of the wave (`pos`). The function adds these starting coordinates to the first item of `precomputed_wave`.

For each subsequent tick of the wave, the function loops through the LED coordinates for the previous tick and calculates the coordinates of each LED that should be illuminated for the next tick. The function stores these coordinates in a new list called `tick_array`, and adds `tick_array` to `precomputed_wave`.

The function uses simple arithmetic to calculate the coordinates of each LED based on the direction of the wave (`pos`). For example, if the wave is moving from left to right (`pos = 3`), the function increments the x-coordinate of each LED in the previous tick by 1. The function then adds `tick_array` to `precomputed_wave`.

The function returns the `precomputed_wave` list, which contains the LED coordinates for each tick of the wave.

## Example Usage

```py
# Compute precomputed_wave for a wave moving from up to down with a duration of 5 ticks
precomputed_wave = precomputeWave(0, 5)
```

In the example above, we call the `precomputeWave` function to compute an array of LED coordinates for a wave moving from up to down with a duration of 5 ticks.

## Exceptions

- The `precomputeWave` function assumes that the LED display is represented as a rectangular grid of LEDs with a width of `board_width` and a height of `board_height`. If the LED display is represented differently, the `precomputeWave` function should be modified accordingly.

- The `precomputeWave` function assumes that the `board_width` and `board_height` constants are defined properly. If these constants are not defined properly, the `precomputeWave` function may not work as expected.

- The `precomputeWave` function assumes that the `setPixelColour` function is defined properly and that it can set the color of a single LED on the LED display. If the `setPixelColour` function is not defined properly or if the LED display is represented differently, the `precomputeWave` function should be modified accordingly.
