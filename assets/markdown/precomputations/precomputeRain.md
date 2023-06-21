# precomputeRain function

## Overview

The `precomputeRain` function computes an array of LED coordinates for a singular raindrop pattern, given the starting x-coordinate of the raindrop. The function returns the coordinates of the raindrop for a fixed duration of 20 ticks.

## Function Signature

```py
def precomputeRain(x: int) -> List[List[List[int, int]]]:
    pass
```

## Parameters

- `x` = `(int)`: An integer representing the x-coordinate of the top of the raindrop.

## Return Value

- `List[List[List[int, int]]]`: A three-dimensional list representing the LED coordinates for each tick of the raindrop. Each item in the list represents a tick of the raindrop, and each item in the second-level list represents an LED that should be illuminated for that tick. The third-level list contains the x and y coordinates of the LED.

## Function Description

The `precomputeRain` function computes an array of LED coordinates for a singular raindrop pattern, given the starting x-coordinate of the raindrop. The function first sets the duration of the raindrop to 20 ticks and initializes the y-coordinate of the top of the raindrop to 19.

The function then creates an empty list called `precomputed_wave` to store the LED coordinates for each tick of the raindrop. The x and y coordinates of the top of the raindrop are added to the first item of `precomputed_wave`.

For each subsequent tick of the raindrop, the function decrements the y-coordinate of the top of the raindrop by 1 and adds the new coordinates to the `precomputed_wave` list.

Finally, the function returns the `precomputed_wave` list.

## Example Usage

```py
# Compute precomputed_wave for a singular raindrop starting at x=5
precomputed_wave = precomputeRain(5)
```

In the example above, we call the `precomputeRain` function to compute an array of LED coordinates for a singular raindrop starting at $x=5$.

## Exceptions

- The `precomputeRain` function assumes that the LED display is represented as a rectangular grid of LEDs with a width of `board_width` and a height of `board_height`. If the LED display is represented differently, the `precomputeRain` function should be modified accordingly.

- The `precomputeRain` function assumes that the `board_width` and `board_height` constants are defined properly. If these constants are not defined properly, the `precomputeRain` function may not work as expected.

- The `precomputeRain` function assumes that the `setPixelColour` function is defined properly and that it can set the color of a single LED on the LED display. If the `setPixelColour` function is not defined properly or if the LED display is represented differently, the `precomputeRain` function should be modified accordingly.
