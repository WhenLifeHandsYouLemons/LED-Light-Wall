# setAllPixelsColour function

## Overview

The `setAllPixelsColour` function takes an RGB color as a tuple of three integers, sets all pixels to the specified color, and updates the LED display. This function is useful for applications that require setting the color of the entire LED display.

## Function Signature

```py
def setAllPixelsColour(colour: Tuple[int, int, int]) -> None:
    pass
```

## Parameters

- `colour` = `(Tuple[int, int, int])`: A tuple of three integers representing the RGB color. The first integer represents the red component, the second integer represents the green component, and the third integer represents the blue component. Each component must be an integer between 0 and 255, inclusive.

## Return Value

- None

## Function Description

The `setAllPixelsColour` function takes an RGB color as a tuple of three integers, `colour`, which represents the color to set all the pixels to. The function sets all pixels to the specified color and updates the LED display.

The function first calls the `RGBToHex` function to convert the `colour` tuple to its corresponding hexadecimal value. The function then uses the `fill()` method of the `pixel_framebuf` object to set all pixels to the specified color, and the `display()` method to update the LED display with the new color.

## Example Usage

```py
# Set all pixels to red
setAllPixelsColour((255, 0, 0))
```

In the example above, we call the `setAllPixelsColour` function with the tuple `(255, 0, 0)`, which represents the RGB color red. The function sets all pixels to red and updates the LED display.

## Exceptions

- `TypeError`: If the `colour` parameter is not a tuple of three integers, a `TypeError` is raised.

- `ValueError`: If any of the color components in the `colour` tuple is not an integer between 0 and 255, inclusive, a `ValueError` is raised.

## Notes

- The `setAllPixelsColour` function assumes that the LED display is represented by the `pixel_framebuf` object and that it has the `fill()` and `display()` methods. If the LED display is represented differently or if the display methods have different names, the function should be modified accordingly.

- The `setAllPixelsColour` function does not perform any error checking beyond checking that the `colour` parameter is a tuple of three integers. It is the responsibility of the calling code to ensure that the input color is valid and within the appropriate range for the RGB color space.