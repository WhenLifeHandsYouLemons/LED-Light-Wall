# drawRect function

## Overview

The `drawRect` function draws a rectangle with a specified width, height, color, and style on a pixel frame buffer. The function outputs the rectangle on the pixel frame buffer.

## Function Signature

```py
def drawRect(x: int,
             y: int,
             width: int,
             height: int,
             colour: Tuple[int, int, int],
             filled: bool) -> None:
    pass
```

## Parameters

- `x` = `(int)`: An integer representing the x coordinate of the top-left corner of the rectangle.

- `y` = `(int)`: An integer representing the y coordinate of the top-left corner of the rectangle.

- `width` = `(int)`: An integer representing the width of the rectangle.

- `height` = `(int)`: An integer representing the height of the rectangle.

- `colour` = `(Tuple[int, int, int])`: A tuple of three integers representing the RGB color values for the rectangle.

- `filled` = `(bool)`: A boolean value representing the style of the rectangle. If `filled` is `True`, the rectangle is filled; otherwise, it is hollow.

## Return Value

- None

## Function Description

The `drawRect` function draws a rectangle on a pixel frame buffer using the `rect` or `fill_rect` function from the `pixel_framebuf` library. The functiontakes in the x and y coordinates of the top-left corner of the rectangle, the width and height of the rectangle, the RGB color values of the rectangle, and a boolean value representing the style of the rectangle.

If `filled` is `True`, the function draws a filled rectangle using the `fill_rect` function. Otherwise, the function draws a hollow rectangle using the `rect` function.

After drawing the rectangle, the function calls the `display` function from the `pixel_framebuf` library to update the pixel frame buffer with the newly drawn rectangle.

Finally, the function completes when the rectangle has been drawn on the pixel frame buffer.

## Example Usage

```py
# Draw a filled rectangle starting at (5, 5) with a width of 10, a height of 15, and the color (255, 0, 0)
drawRect(5, 5, 10, 15, [255, 0, 0], True)

# Draw a hollow rectangle starting at (0, 0) with a width of 20, a height of 10, and the color (0, 255, 0)
drawRect(0, 0, 20, 10, [0, 255, 0], False)
```

In the examples above, we call the `drawRect` function to draw a filled rectangle starting at $(5, 5)$ with a width of 10, a heightof 15, and the color $(255, 0, 0)$ and to draw a hollow rectangle starting at $(0, 0)$ with a width of 20, a height of 10, and the color $(0, 255, 0)$ on the pixel frame buffer.

## Exceptions

- The `drawRect` function assumes that the pixel frame buffer is represented as a rectangular grid of pixels with a width of `board_width` and a height of `board_height`. If the pixel frame buffer is represented differently, the `drawRect` function should be modified accordingly.

- The `drawRect` function assumes that the RGB color values are integers between 0 and 255. If the RGB color values are represented differently, the `drawRect` function should be modified accordingly.

- The `drawRect` function assumes that the `rect`, `fill_rect`, and `display` functions are defined properly in the `pixel_framebuf` library. If any of these functions is not defined properly, the `drawRect` function should be modified accordingly.

- The coordinate system starts from the top left and the first LED is at position $(0, 0)$.