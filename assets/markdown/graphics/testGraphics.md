# testGraphics function

## Overview

The `testGraphics` function is a Python function that tests various graphics functions. This function is useful for developers who are working on graphics-intensive applications and want to ensure that their graphics functions are working correctly.

## Function Signature

```py
def testGraphics(delay: float = 1) -> None:
    pass
```

## Parameters

- `delay` = `(float)`: The amount of time, in seconds, to wait between each graphics test. This parameter is optional and defaults to 1 second if not provided.

## Return Value

- `None`: The function does not return anything.

## Function Description

The `testGraphics` function tests several graphics functions by calling them with various parameters. The following graphics functions are called within the `testGraphics` function:

- `drawLine`: draws a line on the screen using the specified parameters.
- `drawStraightLine`: draws a straight line on the screen using the specified parameters.
- `drawRect`: draws a rectangle on the screen using the specified parameters.
- `drawCircle`: draws a circle on the screen using the specified parameters.
- `scrollText`: scrolls a text message across the screen using the specified parameters.
- `setAllPixelsColour`: sets the color of all pixels on the screen to the specified color.

The function first calls `drawLine` to draw a line on the screen, followed by `drawStraightLine` to draw two straight lines on the screen, one horizontal and one vertical. Next, the function calls `drawRect` twice to draw two rectangles on the screen, one filled and one unfilled. After that, the function calls `drawCircle` to draw a circle on the screen.

The function then waits for the amount of time specified by the `delay` parameter, and clears the screen by calling `setAllPixelsColour` to set the color of all pixels on the screen to black. Finally, the function calls `scrollText` to scroll the text "Text" across the screen in the color red, and clears the screen again by calling `setAllPixelsColour` with the color black.

## Example Usage

```py
# Set the delay time to 0.5 seconds
testGraphics(0.5)
```

In the example above, we call the `testGraphics` function with a delay time of 0.5 seconds. This will cause the function to wait for 0.5 seconds between each graphics test.

## Notes

- This function assumes that the `pixel_framebuf` and `pixels` variables have been initialized correctly with the appropriate values for the screen being used. If these variables are not set or are set incorrectly, the function may not display graphics correctly or at all.

- The `COLOURS` dictionary should be set up with the appropriate color values for the screen being used. If the color values are not set up correctly, the graphics displayed by the function may not be the expected colors.

- The `scrollText` function requires a relatively high refresh rate to display smoothly. If the refresh rate is too slow, the text may appear choppy or difficult to read.

- The `delay` parameter determines the amount of time the function waits between each graphics test. If this value is set too low, the graphics may not display correctly or at all. If this value is set too high, the function may take a long time to complete.

- The `testGraphics` function does not perform any error checking on the input values or variables used within the function. It is the responsibility of the calling code to ensure that the input values and variables are within the appropriate range and set up correctly for the screen being used.