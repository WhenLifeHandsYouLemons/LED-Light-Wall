# drawCircle function

## Overview

The `drawCircle` function draws a circle with a specified center point, radius, and color on a pixel frame buffer. The function outputs the circle on the pixel frame buffer.

## Function Signature

```py
def drawCircle(x: int,
               y: int,
               radius: int,
               colour: Tuple[int, int, int]) -> None:
    pass
```

## Parameters

- `x` = `(int)`: An integer representing the x coordinate of the center of the circle.

- `y` = `(int)`: An integer representing the y coordinate of the center of the circle.

- `radius` = `(int)`: An integer representing the radius of the circle.

- `colour` = `(Tuple[int, int, int])`: A tuple of three integers representing the RGB color values for the circle.

## Return Value

- None

## Function Description

The `drawCircle` function draws a circle on a pixel frame buffer using the `circle` function from the `pixel_framebuf` library. The function takes in the x and y coordinates of the center of the circle, the radius of the circle, and the RGB color values of the circle.

After drawing the circle, the function calls the `display` function from the `pixel_framebuf` library to update the pixel frame buffer with the newly drawn circle.

Finally, the function completes when the circlehas been drawn on the pixel frame buffer.

## Example Usage

```py
# Draw a circle with center at (10, 10), radius of 5, and color (255, 0, 0)
drawCircle(10, 10, 5, [255, 0, 0])
```

In the example above, we call the `drawCircle` function to draw a circle with a center at $(10, 10)$, radius of 5, and color $(255, 0, 0)$ on the pixel frame buffer.

## Exceptions

- The `drawCircle` function assumes that the pixel frame buffer is represented as a rectangular grid of pixels with a width of `board_width` and a height of `board_height`. If the pixel frame buffer is represented differently, the `drawCircle` function should be modified accordingly.

- The `drawCircle` function assumes that the RGB color values are integers between 0 and 255. If the RGB color values are represented differently, the `drawCircle` function should be modified accordingly.

- The `drawCircle` function assumes that the `circle` and `display` functions are defined properly in the `pixel_framebuf` library. If either of these functions is not defined properly, the `drawCircle` function should be modified accordingly.

- The coordinate system starts from the top left and the first LED is at position $(0, 0)$.