# drawText function

## Overview

The `drawText` function draws text with a specified color at a specified location on a pixel frame buffer. The function outputs the text on the pixel frame buffer.

## Function Signature

```py
def drawText(text: str,
             x: int,
             y: int,
             colour: Tuple[int, int, int]) -> None:
    pass
```

## Parameters

- `text` = `(str)`: A string representing the text to be drawn on the pixel frame buffer.

- `x` = `(int)`: An integer representing the x coordinate of the top-left corner of the text.

- `y` = `(int)`: An integer representing the y coordinate of the top-left corner of the text.

- `colour` = `(Tuple[int, int, int])`: A list of three integers representing the RGB color values for the text.

## Return Value

- None

## Function Description

The `drawText` function draws text on a pixel frame buffer using the `text` function from the `pixel_framebuf` library. The function takes in the text to be drawn, the x and y coordinates of the top-left corner of the text, and the RGB color values of the text.

After drawing the text, the function calls the `display` function from the `pixel_framebuf` library to update the pixel frame buffer with the newly drawn text.

Finally, the function completes when the text has been drawn on the pixel frame buffer.

## Example Usage

```py
# Draw the text "Hello, world!" at (5, 5) with the color (255, 0, 0)
drawText("Hello, world!", 5, 5, [255, 0, 0])
```

In the example above, we call the `drawText` function to draw the text "Hello, world!" at $(5, 5)$ with the color $(255, 0, 0)$ on the pixel frame buffer.

## Exceptions

- The `drawText` function assumes that the pixel frame buffer is represented as a rectangular grid of pixels with a width of `board_width` and a height of `board_height`. If the pixel frame buffer is represented differently, the `drawText` function should be modified accordingly.

- The `drawText` function assumes that the RGB color values are integers between 0 and 255. If the RGB color values are represented differently, the `drawText` function should be modified accordingly.

- The `drawText` function assumes that the `text` and `display` functions are defined properly in the `pixel_framebuf` library. If either of these functions is not defined properly, the `drawText` function should be modified accordingly.

- The coordinate system starts from the top left and the first LED is at position $(0, 0)$.