# startup function

## Overview

The `startup` function is a utility function that sets the color of all pixels on the LED display to each of the colors in the `colours` dictionary in sequence. This function is useful for verifying that the LED display is working properly and that the colors are being displayed correctly.

## Function Signature

```py
def startup() -> None:
    pass
```

## Return Value

- None

## Function Description

The `startup` function sets the color of all pixels on the LED display to each of the colors in the `colours` dictionary in sequence. The function first sets the color of all pixels to red, waits for one second using the `time.sleep()` function, then sets the color of all pixels to orange, waits for one second, and so on, until the selected colors in the `colours` dictionary have been displayed.

The function uses the `setAllPixelsColour` function to set the color of all pixels to the specified color. The `time.sleep()` function is used to pause the program for one second between each color change.

## Example Usage

```py
# Display all colors in the colours dictionary
startup()
```

In the example above, we call the `startup` function to display all colors in the `colours` dictionary on the LED display.

## Exceptions

- None

## Notes

- The `startup` function assumes that the `setAllPixelsColour` function is defined properly and that it can set the color of all pixels on the LED display. If the `setAllPixelsColour` function is not defined properly or if the LED display is represented differently, the `startup` function should be modified accordingly.

- The `startup` function is intended as a utility function for testing and debugging purposes. It may not be necessary for the final version of the program and can be removed if not needed.
