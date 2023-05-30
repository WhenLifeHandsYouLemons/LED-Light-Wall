# precomputeColours function

## Overview

The `precomputeColours` function takes in a precomputed wave array and calculates an array of crest and fade colors for each LED in the wave. The function outputs the updated wave array with crest and fade colors included.

## Function Signature

```python
def precomputeColours(input_wave: List[List[List[int, int]]],
                      i_color: List[int, int, int],
                      e_color: List[int, int, int],
                      fade: int
                      ) -> List[List[List[int, int, List[int, int, int]]]]:
    pass
```

## Parameters

- `input_wave` = `(List[List[List[int, int]]])`: A three-dimensional list representing the LED coordinates for each tick of the wave.

- `i_color` = `(List[int, int, int])`: A list representing the initial color of the crest in RGB format.

- `e_color` = `(List[int, int, int])`: A list representing the end color of the crest in RGB format.

- `fade` = `(int)`: An integer representing the duration of the fade in ticks.

## Return Value

- `List[List[int, int, List[int, int, int]]]`: A four-dimensional list representing the LED coordinates and colors for each tick of the wave, including crest and fade colors. Each top-level item in the list represents a tick of the wave, and each item in the second-level list represents an LED that should be illuminated for that tick. The third-level listcontains the x and y coordinates of the LED, and a list that contains the RGB color values for the LED.

## Function Description

The `precomputeColours` function first creates a deep copy of the input wave array to avoid modifying the original values. The function then calculates the crest colors for each tick of the wave based on the initial and end colors provided as input.

To calculate the crest colors, the function computes the shift in color for each RGB component per tick, based on the difference between the initial and end colors and the duration of the wave. The function then extends the input wave array to include the crest colors for each LED at each tick.

After computing the crest colors, the function calculates the fade colors for each LED in the wave. The function first adds additional ticks to the wave array to account for the duration of the fade. For each tick in the wave array, the function calculates the fade color for each LED based on the difference between the crest color and the end color, and the duration of the fade.

The function stores the faded LED coordinates and colors in a separate list called `faded_LEDS`. The function then loops through the `faded_LEDS` list and adds the faded LED coordinates and colors to the appropriate tick in the original wave array.

Finally, the function adds all previous tick's LEDs without changing their color to have accurate color mixing. The function returns the updated wave array with crest and fade colors included.

## Example Usage

```py
# Compute precomputed_wave with crest and fade colors for a wave moving from up to down with a duration of 5 ticks, initial color of (255, 0, 0), end color of (0, 255, 0), and a fade duration of 2 ticks
precomputed_wave_with_colour = precomputeColours(precomputed_wave, [255, 0, 0], [0, 255, 0], 2)
```

In the example above, we call the `precomputeColours` function to calculate the crest and fade colors for a precomputed wave array representing a wave moving from up to down with a duration of 5 ticks, an initial color of $(255, 0, 0)$, an end color of $(0, 255, 0)$, and a fade duration of 2 ticks.

## Exceptions

- The `precomputeColours` function assumes that the LED display is represented as a rectangular grid of LEDs with a width of `board_width` and a height of `board_height`. If the LED display is represented differently, the `precomputeColours` function should be modified accordingly.

- The `precomputeColours` function assumes that the `board_width` and `board_height` constants are defined properly. If these constants are not defined properly, the `precomputeColours` function may not work as expected.

- The `precomputeColours` function assumes that the `setPixelColour`function is defined properly and that it can set the color of a single LED on the LED display. If the `setPixelColour` function is not defined properly or if the LED display is represented differently, the `precomputeColours` function should be modified accordingly.
