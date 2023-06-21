# precomputeLines function

## Overview

The `precomputeLines` function computes an array of LED coordinates for a singular straight line pattern, given the starting and ending center coordinates of the line, as well as the width of the line. The function uses the Bresenham's Line Algorithm to calculate the coordinates of the LEDs that should be illuminated for each point on the line. The resulting array can be used to display the line on an LED display.

## Function Signature

```py
def precomputeLines(x: int,
                    y: int,
                    e_x: int,
                    e_y: int,
                    width: int) -> List[List[List[int, int]]]:
    pass
```

## Parameters

- `x` = `(int)`: An integer representing the x-coordinate of the starting center of the line.

- `y` = `(int)`: An integer representing the y-coordinate of the starting center of the line.

- `e_x` = `(int)`: An integer representing the x-coordinate of the ending center of the line.

- `e_y` = `(int)`: An integer representing the y-coordinate of the ending center of the line.

- `width` = `(int)`: An integer representing the width of the line, in LEDs.

## Return Value

- `List[List[List[int, int]]]`: A three-dimensional list representing the LED coordinates for each point on the line. Each top-level item in the list represents a point on the line, and each item in the second-level list represents an LED that should be illuminated for that point. The third-level list contains the x and y coordinates of the LED.

## Function Description

The `precomputeLines` function computes an array of LED coordinates for a singular straight line pattern, given the starting and ending center coordinates of the line, as well as the width of the line.

The function calculates the slope of the line, `m`, then checks whether the line has a steep or shallow gradient. If it's shallow, then the function will iterate over the x-coordinates of the line. Otherwise, the function will iterate over the y-coordinates of the line.

For each point on the line, the function uses the Bresenham's Line Algorithm to calculate the coordinates of the LEDs that should be illuminated for that point.

## Example Usage

```py
# Compute precomputed_wave for a singular straight line from (0, 0) to (5, 5) with a width of 3 LEDs
precomputed_wave = precomputeLines(0, 0, 5, 5, 3)
```

In the example above, we call the `precomputeLines` function to compute an array of LED coordinates for a singular straight line from $(0, 0)$ to $(5, 5)$ with a width of 3 LEDs.

## Exceptions

- The `precomputeLines` function assumes that the LED display is represented as a rectangular grid of LEDs with a width of `board_width` and a height of `board_height`. If the LED display is represented differently, the `precomputeLines` function should be modified accordingly.

- The `precomputeLines` function assumes that the `board_width` and `board_height` constants are defined properly. If these constants are not defined properly, the `precomputeLines` function may not work as expected.

- The `precomputeLines` function assumes that the `setPixelColour` function is defined properly and that it can set the color of a single LED on the LED display. If the `setPixelColour` function is not defined properly or if the LED display is represented differently, the `precomputeLines` function should be modified accordingly.

- The `precomputeLines` function uses the Bresenham's Line Algorithm to calculate the coordinates of the LEDs that should be illuminated for each point on the line. While this algorithm is efficient, it may not produce perfectly straight lines in some cases. If perfectly straight lines are required, a different algorithm may need to be used.

- The `precomputeLines` function may not work as expected if the starting and ending coordinates of the line do not form a straight line. In this case, the resulting LED coordinates may not form a straight line on the LED display.

- The `precomputeLines` function assumes that the width of the line is an odd integer. If an even integer is supplied, the function will round down to the nearest odd integer.

- The `precomputeLines` function assumes that the starting and ending coordinates of the line are within the bounds of the LED display. If the coordinates are outside the bounds of the LED display, the function may not work as expected.
