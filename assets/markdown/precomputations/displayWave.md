# displayWave function

## Overview

The `displayWave` function takes in a wave array (which can be a merged or a single wave array) and displays it on an LED matrix. The function outputs the wave on the LED matrix with a specified delay between each tick.

## Function Signature

```py
def displayWave(wave_array: List[List[List[List[int]]]], delay: float) -> None:
    pass
```

## Parameters

- `wave_array` = `(List[List[List[int, int, List[int, int, int]]]])`: A four-dimensional list representing the LED coordinates and colors for each tick of the wave. Each top-level item in the list represents a wave, and each item in the second-level list represents a tick of the wave. The third-level list contains the x and y coordinates of the LED, and the fourth-level list contains the RGB color values for the LED.

- `delay` = `(float)`: A floating point number representing the delay in seconds between each tick of the wave.

## Return Value

- None

## Function Description

The `displayWave` function loops through each tick in the `wave_array`, and for each tick, it loops through each LED in the tick and sets the color of the corresponding LED on the LED matrix using the `setPixelsColour` function and the `getLED` function.

After setting the colorsof the LEDs for the current tick, the function calls `pixels.show()` to update the display and `time.sleep(delay)` to pause for the specified delay between each tick.

Finally, the function completes when all ticks in all waves in the wave array have been displayed.

## Example Usage

```py
# Display a wave array with a delay of 0.5 seconds between each tick
displayWave(wave_array, 0.5)
```

In the example above, we call the `displayWave` function to display a wave array on an LED matrix with a delay of 0.5 seconds between each tick.

## Exceptions

- The `displayWave` function assumes that the LED display is represented as a rectangular grid of LEDs with a width of `board_width` and a height of `board_height`. If the LED display is represented differently, the `displayWave` function should be modified accordingly.

- The `displayWave` function assumes that all waves in the `wave_array` have the same number of ticks and that each LED is represented as a list with three items: the x and y coordinates, and the RGB color values. If the input wave arrays do not meet these assumptions, the `displayWave` function may not work as expected.

- The `displayWave` function assumes that the RGB color values are integers between 0 and 255. If the RGB color values are represented differently, the `displayWave` function should be modified accordingly.

- The`displayWave` function assumes that the `setPixelsColour` function is defined properly and that it can set the color of a single LED on the LED display. If the `setPixelsColour` function is not defined properly or if the LED display is represented differently, the `displayWave` function should be modified accordingly.

- The `displayWave` function assumes that the `getLED` function is defined properly and that it can return the LED object for a given x and y coordinate on the LED display. If the `getLED` function is not defined properly or if the LED display is represented differently, the `displayWave` function should be modified accordingly.