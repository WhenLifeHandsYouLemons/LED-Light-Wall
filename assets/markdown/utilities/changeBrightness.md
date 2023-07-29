# changeBrightness function

## Overview

The `changeBrightness` function changes the brightness of the LEDs on the board and returns a tuple of the `pixels` object and `pixel_framebuf` object. This function is useful for applications that require adjusting the brightness of the LEDs or resetting the frame buffer when displaying text.

## Function Signature

```py
def changeBrightness(brightness: float) -> Tuple[neopixel.NeoPixel, PixelFramebuffer]:
    pass
```

## Parameters

- `brightness` = `(float)`: The desired brightness level of the LEDs. This must be a float value between $0$ and $1$.

## Return Value

- `Tuple[neopixel.NeoPixel, PixelFramebuffer]`: A tuple containing the `pixels` object and `pixel_framebuf` object. The `pixels` object is an instance of the `neopixel.NeoPixel` class, which represents the LED pixels on the board. The `pixel_framebuf` object is an instance of the `PixelFramebuffer` class, which provides a frame buffer for the LED pixels.

## Function Description

The `changeBrightness` function takes in a float value, `brightness`, which represents the desired brightness level of the LEDs. The function creates a `neopixel.NeoPixel` object named `pixels` with the specified brightness level and other parameters. It also creates a `PixelFramebuffer` object named `pixel_framebuf` with the `pixels` object and other parameters.

Finally, the function returns a tuple containing the `pixels` object and `pixel_framebuf` object.

## Example Usage

```py
# Set the brightness level to 0.5
brightness = 0.5

# Change the brightness of the LEDs
pixels, pixel_framebuf = changeBrightness(brightness)

# Set all LEDs to red
pixels.fill((255, 0, 0))

# Display the LEDs
pixels.show()
```

In the example above, we set the `brightness` variable to 0.5 and call the `changeBrightness` function with this value. The function returns a tuple containing the `pixels` object and `pixel_framebuf` object. We then set all the LEDs to red using the `fill` method of the `pixels` object, and display them using the `show` method of the `pixel_framebuf` object.

## Exceptions

- `ValueError`: If `brightness` is not a float value between 0 and 1, a `ValueError` is raised.

## Notes

- The `changeBrightness` function assumes that the `DATA_PIN`, `BOARD_WIDTH`, and `BOARD_HEIGHT` variables have been set to the correct values for the LED board being used. If these variables are not set or are set incorrectly, the function may not work as expected.

- If you want to adjust the brightness of the LEDs without resetting the frame buffer, you can simply call the `neopixel.NeoPixel` constructor with the new `brightness` value.