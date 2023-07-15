# displayRandomPatterns function

## Overview

The `displayRandomPatterns` function takes in a pixel_frambuf, merged_wave_array, non_merged_array and displays it on an LED matrix. The function outputs the patterns on the LED matrix.

## Function Signature

```py
def displayRandomPatterns(pixel_framebuf,
                          merged_array: List[List[List[int, int, List[int, int, int]]]],
                          non_merged_array: List[str]) -> None:
    pass
```

## Parameters

- `pixel_framebuf`: A Neopixel pixel_framebuffer object to display the text and images on.

- `merged_wave_array` = `(List[List[List[int, int, List[int, int, int]]]])`: A four-dimensional list representing the LED coordinates and colors for each tick of the wave. Each top-level item in the list represents a wave, and each item in the second-level list represents a tick of the wave. The third-level list contains the x and y coordinates of the LED, and the fourth-level list contains the RGB color values for the LED.

- `non_merged_array` = `(List[str])`: A one-dimensional list representing how many strings of text and images that need to be displayed. The items are of type `str`.

## Return Value

- None

## Function Description

The `displayRandomPatterns` function loops through each tick in the `merged_wave_array`, and for each tick, it loops through each LED in the tick and sets the color of the corresponding LED on the LED matrix using the `setPixelsColour` function and the `getLED` function.

After setting the colors of the LEDs for the current tick, the function calls `pixels.show()` to update the display between each tick.

Finally, the function completes when all ticks in all waves in the wave array have been displayed.

## Example Usage

```py
# Display a wave array with a delay of 0.5 seconds between each tick
displayRandomPatterns(pixel_framebuf, merged, non_merged)
```

In the example above, we call the `displayRandomPatterns` function to display a wave array and then text and images on an LED matrix.

## Exceptions

- The `displayRandomPatterns` function assumes that the LED display is represented as a rectangular grid of LEDs with a width of `board_width` and a height of `board_height`. If the LED display is represented differently, the `displayRandomPatterns` function should be modified accordingly.

- The `displayRandomPatterns` function assumes that all waves in the `merged_wave_array` have the same number of ticks and that each LED is represented as a list with three items: the x and y coordinates, and the RGB color values. If the input wave arrays do not meet these assumptions, the `displayRandomPatterns` function may not work as expected.

- The `displayRandomPatterns` function assumes that the RGB color values are integers between 0 and 255. If the RGB color values are represented differently, the `displayRandomPatterns` function should be modified accordingly.

- The`displayRandomPatterns` function assumes that the `setPixelsColour` function is defined properly and that it can set the color of a single LED on the LED display. If the `setPixelsColour` function is not defined properly or if the LED display is represented differently, the `displayRandomPatterns` function should be modified accordingly.

- The `displayRandomPatterns` function assumes that the `getLED` function is defined properly and that it can return the LED object for a given x and y coordinate on the LED display. If the `getLED` function is not defined properly or if the LED display is represented differently, the `displayRandomPatterns` function should be modified accordingly.
