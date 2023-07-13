# drawLine function

## Overview

The `drawLine` function draws a single line between two points with a specified color on a pixel frame buffer. The function outputs the line on the pixel frame buffer.

## Function Signature

```py
def drawLine(start_x: int,
             start_y: int,
             end_x: int,
             end_y: int,
             colour: Tuple[int, int, int]) -> None:
    pass
```

## Parameters

- `start_x` = `(int)`: An integer representing the x coordinate of the start point of the line.

- `start_y` = `(int)`: An integer representing the y coordinate of the start point of the line.

- `end_x` = `(int)`: An integer representing the x coordinate of the end point of the line.

- `end_y` = `(int)`: An integer representing the y coordinate of the end point of the line.

- `colour` = `(Tuple[int, int, int])`: A tuple of three integers representing the RGB color values for the line.

## Return Value

- None

## Function Description

The `drawLine` function draws a single line between two points on a pixel frame buffer using the `line` function from the `pixel_framebuf` library. The function takes in the x and y coordinates of the start and end points of the line, as well as the RGB color values of the line.

After drawing the line, the function calls the `display` function from the `pixel_framebuf` library to update the pixel frame buffer with the newly drawn line.

Finally, the function completes when the line has been drawn on the pixel frame buffer.

## Example Usage

```py
# Draw a line from (0, 0) to (10, 10) with the color (255, 0, 0)
drawLine(0, 0, 10, 10, [255, 0, 0])
```

In the example above, we call the `drawLine` function to draw a line from the point $(0, 0)$ to the point $(10, 10)$ with the color $(255, 0, 0)$ on the pixel frame buffer.

## Exceptions

- The `drawLine` function assumes that the pixel frame buffer is represented as a rectangular grid of pixels with a width of `framebuf_width` and a height of `framebuf_height`. If the pixel frame buffer is represented differently, the `drawLine` function should be modified accordingly.

- The `drawLine` function assumes that the RGB color values are integers between 0 and 255. If the RGB color values are represented differently, the `drawLine` function should be modified accordingly.

- The `drawLine` function assumes that the `line` and `display` functions are defined properly in the `pixel_framebuf` library. If either of these functions is not defined properly, the `drawLine` function should be modified accordingly.

- The coordinate system starts from the top left and the first LED is at position $(0, 0)$.