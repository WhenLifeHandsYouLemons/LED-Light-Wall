# setPixelsColour function

## Overview

The `setPixelsColour` function takes an RGB color as a tuple of three integers, and sets all pixels in a specified range to the specified color. This function is useful for applications that require setting the color of a specific range of pixels on the LED display.

## Function Signature

```py
def setPixelsColour(colour: Tuple[int, int, int],
                    pixel_index_start: int,
                    pixel_index_end: Optional[int] = None) -> None:
    pass
```

## Parameters

- `colour` = `(Tuple[int, int, int])`: A tuple of three integers representing the RGB color. The first integer represents the red component, the second integer represents the green component, and the third integer represents the blue component. Each component must be an integer between 0 and 255, inclusive.

- `pixel_index_start` = `(int)`: An integer representing the index of the first pixel to set to the specified color. This must be an integer between 0 and the total number of pixels minus 1, inclusive.

- `pixel_index_end` = `(int)`: An **optional** integer representing the index of the last pixel to set to the specified color. If this parameter is not provided, only the pixel at `pixel_index_start` will be set to the specified color.

## Return Value

- None

## Function Description

The `setPixelsColour` function takes an RGB color as a tuple of three integers, `colour`, the index of the first pixel to set to the specified color, `pixel_index_start`, and an optional index of the last pixel to set to the specified color, `pixel_index_end`. The function sets all pixels in the specified range to the specified color.

If `pixel_index_end` is not provided, the function sets the color of a single pixel at the index `pixel_index_start` to the specified color. Otherwise, the function uses a loop to set the color of all pixels between `pixel_index_start` and `pixel_index_end`, inclusive, to the specified color.

## Example Usage

```py
# Set pixels 5-7 to red
setPixelsColour((255, 0, 0), 5, 7)
```

In the example above, we call the `setPixelsColour` function with the tuple `(255, 0, 0)` to set the color to red, and `pixel_index_start` equal to 5 and `pixel_index_end` equal to 7 to set the color of pixels 5, 6, and 7 to red.

```py
# Set pixel 3 to green
setPixelsColour((0, 255, 0), 3)
```

In the example above, we call the `setPixelsColour` function with`pixel_index_start` equal to 3 and no `pixel_index_end` specified, so the function sets the color of only pixel 3 to green.

## Exceptions

- `TypeError`: If the `colour` parameter is not a tuple of three integers, or if `pixel_index_start` or `pixel_index_end` (if provided) is not an integer, a `TypeError` is raised.

- `ValueError`: If any of the color components in the `colour` tuple is not an integer between 0 and 255, inclusive, or if `pixel_index_start` or `pixel_index_end` (if provided) is not within the appropriate range for the LED display, a `ValueError` is raised.

## Notes

- The `setPixelsColour` function assumes that the LED display is represented by the `pixels` object and that it has the ability to set individual pixel colors. If the LED display is represented differently or if the display methods have different names, the function should be modified accordingly.

- The `setPixelsColour` function does not perform any error checking beyond checking that the input parameters are of the correct type and within the appropriate range. It is the responsibility of the calling code to ensure that the input values are valid.

- The coordinate system starts from the bottom left and the first LED is at position $(0, 0)$.