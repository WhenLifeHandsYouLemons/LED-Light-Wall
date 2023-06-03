# mergeWaves function

## Overview

The `mergeWaves` function takes in an array of wave arrays and merges them into a single master array to be displayed. The function outputs a merged wave array with duplicate LED coordinates merged and the colors averaged.

## Function Signature

```py
def mergeWaves(wave_arrays: List[List[List[int, int, List[int, int]]]]) -> List[List[int, int, List[int, int, int]]]:
    pass
```

## Parameters

- `wave_arrays` = `(List[List[List[int, int, List[int, int, int]]]])`: A four-dimensional list representing the LED coordinates and colors for each tick of each wave. Each top-level item in the list represents a wave, and each item in the second-level list represents a tick of the wave. The third-level list contains the x and y coordinates of the LED, and the fourth-level list contains the RGB color values for the LED.

## Return Value

- `merged_wave_array` = `(List[List[int, int, List[int, int, int]]])`: A three-dimensional list representing the merged LED coordinates and colors for each tick of the waves. Each top-level item in the list represents a tick of the wave, and each item in the second-level list represents an LED that should be illuminated for that tick. The third-level list contains the x and y coordinates of the LED, and a list containing the RGB color values for the LED.

## Function Description

The `mergeWaves` function firstfinds the longest number of ticks across all the input wave arrays. It then makes all the waves have the same number of ticks by appending copies of the last tick to the end of the wave array until it reaches the desired length.

The function then sorts all the LEDs for every wave into one singular array by ticks. It creates a `sorted_wave_array` that contains all the LED coordinates and colors sorted by ticks.

After sorting the LED coordinates, the function merges all duplicates in each tick separately. It creates a `merged_wave_array` that contains the merged LED coordinates and colors for each tick of the waves. The function loops through each tick in the `sorted_wave_array` and merges duplicate LED coordinates by averaging their colors. It keeps track of the used coordinates to avoid merging the same LED multiple times.

Finally, the function returns the `merged_wave_array` with duplicate LED coordinates merged and the colors averaged.

## Example Usage

```py
# Merge wave arrays into a single wave array for display
merged_wave_array = mergeWaves([wave_array1, wave_array2, wave_array3])
```

In the example above, we call the `mergeWaves` function to merge three wave arrays into a single wave array for display.

## Exceptions

- The `mergeWaves` function assumes that the LED display is represented as a rectangular grid of LEDs with a width of `board_width` and a height of `board_height`. If the LED display is represented differently, the`mergeWaves` function should be modified accordingly.

- The `mergeWaves` function assumes that all waves have the same number of LEDs and that each LED is represented as a list with three items: the x and y coordinates, and the RGB color values. If the input wave arrays do not meet these assumptions, the `mergeWaves` function may not work as expected.

- The `mergeWaves` function assumes that the RGB color values are integers between 0 and 255. If the RGB color values are represented differently, the `mergeWaves` function should be modified accordingly.

- The `mergeWaves` function assumes that the `setPixelColour` function is defined properly and that it can set the color of a single LED on the LED display. If the `setPixelColour` function is not defined properly or if the LED display is represented differently, the `mergeWaves` function should be modified accordingly.