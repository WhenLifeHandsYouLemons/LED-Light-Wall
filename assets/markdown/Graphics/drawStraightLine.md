# drawStraightLine function

## Overview

The `drawStraightLine` function draws a straight line with a specified length, color, and orientation on a pixel frame buffer. The function outputs the line on the pixel frame buffer.

## Function Signature

```py
def drawStraightLine(x: int,
                     y: int,
                     length: int,
                     colour: Tuple[int, int, int],
                     horizontal: bool) -> None:
    pass
```

## Parameters

- `x` = `(int)`: An integer representing the x coordinate of the start point of the line.

- `y` = `(int)`: An integer representing the y coordinate of the start point of the line.

- `length` = `(int)`: An integer representing the length of the line.

- `colour` = `(Tuple[int, int, int])`: A tuple of three integers representing the RGB color values for the line.

- `horizontal` = `(bool)`: A boolean value representing the orientation of the line. If `horizontal` is `True`, the line is horizontal; otherwise, it is vertical.

## Return Value

- None

## Function Description

The `drawStraightLine` function draws a straight line on a pixel frame buffer using the `hline` or `vline` function from the `pixel_framebuf` library. The function takes in the x and y coordinates of the start point of the line,the length of the line, the RGB color values of the line, and a boolean value representing the orientation of the line.

If `horizontal` is `True`, the function draws a horizontal line from left to right using the `hline` function. Otherwise, the function draws a vertical line from top to bottom using the `vline` function.

After drawing the line, the function calls the `display` function from the `pixel_framebuf` library to update the pixel frame buffer with the newly drawn line.

Finally, the function completes when the line has been drawn on the pixel frame buffer.

## Example Usage

```py
# Draw a horizontal line starting at (0, 0) with a length of 10 and the color (255, 0, 0)
drawStraightLine(0, 0, 10, [255, 0, 0], True)

# Draw a vertical line starting at (5, 5) with a length of 15 and the color (0, 255, 0)
drawStraightLine(5, 5, 15, [0, 255, 0], False)
```

In the examples above, we call the `drawStraightLine` function to draw a horizontal line starting at $(0, 0)$ with a length of 10 and the color $(255, 0, 0)$ and to draw a vertical line starting at $(5, 5)$ with a lengthof 15 and the color $(0, 255, 0)$ on the pixel frame buffer.

## Exceptions

- The `drawStraightLine` function assumes that the pixel frame buffer is represented as a rectangular grid of pixels with a width of `board_width` and a height of `board_height`. If the pixel frame buffer is represented differently, the `drawStraightLine` function should be modified accordingly.

- The `drawStraightLine` function assumes that the RGB color values are integers between 0 and 255. If the RGB color values are represented differently, the `drawStraightLine` function should be modified accordingly.

- The `drawStraightLine` function assumes that the `hline`, `vline`, and `display` functions are defined properly in the `pixel_framebuf` library. If any of these functions is not defined properly, the `drawStraightLine` function should be modified accordingly.

- The coordinate system starts from the top left and the first LED is at position $(0, 0)$.