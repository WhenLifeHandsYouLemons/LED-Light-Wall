# testGraphics function

## Overview

The `testGraphics` function draws various shapes and text on the screen to test the graphics capabilities of the display. The function draws a line, straight line, rectangle, circle, and scrolling text on the screen.

## Function Signature

```py
def testGraphics(delay: float = 1.0) -> None:
    pass
```

## Parameters

- `delay` = `float`: A float value representing the time to wait between each shape or text being drawn on the screen. The default value is 1 second.

## Return Value

- `None`: The function does not return any value.

## Function Description

The `testGraphics` function draws various shapes and text on the screen to test the graphics capabilities of the display.

The function starts by calling the `drawLine` function to draw a diagonal line from $(0, 0)$ to $(3, 2)$ with the color green. The function then calls the `drawStraightLine` function twice to draw a vertical line and a horizontal line with the color blue. The function then calls the `drawRect` function twice to draw a rectangle with the color red and an outlined rectangle with the color orange. Finally, the function calls the `drawCircle` function to draw a circle with the color green.

After drawing all shapes, the function waits for a specified amount of time using the `time.sleep` function and then clears the screen by calling the `setAllPixelsColour` function with the color black. The function then calls the `scrollText` function to scroll the text "Text" on the screen with the color red. The function waits for a specified amount of time between each frame of the scrolling animation and then clears the screen again by calling the `setAllPixelsColour` function with the color black.

## Example Usage

```py
# Test graphics capabilities of the display
testGraphics(0.5)
```

In the example above, we call the `testGraphics` function to draw various shapes and text on the screen and test the graphics capabilities of the display.

## Exceptions

- The `testGraphics` function assumes that the `drawLine`, `drawStraightLine`, `drawRect`, `drawCircle`, `scrollText`, and `setAllPixelsColour` functions are defined properly and can be used to draw on the screen and clear the screen. If these functions are not defined properly, the function may not work as expected.

- The `testGraphics` function assumes that the `delay` parameter is a float value representing the time to wait between each shape or text being drawn on the screen. If the `delay` parameter is not a float value, the function may not work as expected.