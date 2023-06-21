# scrollText function

## Overview

The `scrollText` function animates text scrolling from right to left on a pixel frame buffer. The function outputs the scrolling text on the pixel frame buffer.

## Function Signature

```py
def scrollText(text: str,
               colour: Tuple[int, int, int],
               wait_time: float,
               end_x: int,
               y: int = 5) -> None:
    pass
```

## Parameters

- `end_x` = `(int)`: An integer representing the x coordinate where the scrolling text will stop.

- `y` = `(int)`: An integer representing the y coordinate of the top-left corner of the scrolling text.

- `text` = `(str)`: A string representing the text to be scrolled on the pixel frame buffer.

- `colour` = `(Tuple[int, int, int])`: A tuple of three integers representing the RGB color values for the scrolling text.

- `wait_time` = `(float)`: A floating-point number representing the duration in seconds between each frame of the scrolling text animation.

## Return Value

- None

## Function Description

The `scrollText` function animates the scrolling text on a pixel frame buffer by repeatedly calling the `drawText` function with different x coordinates. The function takes in the x coordinate where the scrolling text will stop, the y coordinate of the top-left corner of the scrolling text, the text to be scrolled,the RGB color values of the scrolling text, and the duration in seconds between each frame of the scrolling text animation.

The `scrollText` function initializes the x coordinate to be off-screen to the right (`board_width + 1`). Then, it enters a loop where it calls the `drawText` function with the current x coordinate, y coordinate, text, and color. After displaying the text, the function waits for the specified duration using the `time.sleep` function and clears the pixel frame buffer by calling the `setAllPixelsColour` function with the color black. Finally, the function decrements the x coordinate by 1 and repeats the loop until the x coordinate is less than or equal to the specified end_x coordinate.

Once the scrolling text animation is complete, the function completes.

## Example Usage

```py
# Animate scrolling text with the message "Hello, world!" in red
# The scrolling text starts at the right edge of the pixel frame buffer and stops at x = 0
# The scrolling text animation waits for 0.1 seconds between each frame
scrollText("Hello, world!", [255, 0, 0], 0.1, 0, 5)
```

In the example above, we call the `scrollText` function to animate scrolling text with the message "Hello, world!" in red on the pixel frame buffer. The scrolling text starts at the right edge of the pixel frame buffer and stops at $x=0$. The scrolling text animation waits for 0.1 seconds between each frame.

## Exceptions

- The `scrollText` function assumes that the pixel frame buffer is represented as a rectangular grid of pixels with a width of `board_width` and a height of `board_height`. If the pixel frame buffer is represented differently, the `scrollText` function should be modified accordingly.

- The `scrollText` function assumes that the RGB color values are integers between 0 and 255. If the RGB color values are represented differently, the `scrollText` function should be modified accordingly.

- The `scrollText` function assumes that the `drawText`, `time.sleep`, and `setAllPixelsColour` functions are defined properly. If any of these functions is not defined properly, the `scrollText` function should be modified accordingly.

- The coordinate system starts from the top left and the first LED is at position $(0, 0)$.
