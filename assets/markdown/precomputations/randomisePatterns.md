# randomisePatterns function

## Overview

The `randomisePatterns` function takes in an array of wave arrays and merges them into a single master array to be displayed. The function outputs a merged wave array with duplicate LED coordinates merged and the colors averaged.

## Function Signature

```py
def randomisePatterns() -> List[List[int, int, List[int, int, int]]], List[str, str]:
    pass
```

## Parameters

- None

## Return Value

- `merged_patterns` = `(List[List[int, int, List[int, int, int]]])`: A three-dimensional list representing the merged LED coordinates and colors for each tick of the waves. Each top-level item in the list represents a tick of the wave, and each item in the second-level list represents an LED that should be illuminated for that tick. The third-level list contains the x and y coordinates of the LED, and a list containing the RGB color values for the LED.

- `non_merge` = `(List[str, str])`: A one dimensional list containing the information for an image or text to be displayed on the board. The list either contains `"text"` or `"image"` and depending on the type, it will display either a random string of text or a random image after the `merged_patterns` are displayed.

## Function Description

The `randomisePatterns` function first chooses random numbers to determine the total number of patterns and the starting colour of the wave.

Then, for every wave pattern, it chooes a random number to get the type of pattern (images and text have a 1/36 chance of occuring), precomputes the wave and colour, then stores it into an array. Depending on the wave pattern chosen, it can choose more random numbers for the following parameters that apply:

- Wave direction
- Starting x and y position
- Ending x and y position
- Ending colour
- Trail length
- Number of rain drops
- Width of the line

The function then sorts the mergable and non-mergable items in the array into two separate arrays and chooses more random numbers for the start times of the mergable wave patterns. It then merges the mergable array along with the start times using the `mergeWaves` function.

Finally, the function returns the `merged_patterns` array and the `non_merge` array to be displayed using the `displayRandomPatterns` function.

## Example Usage

```py
# Get two arrays that have random patterns to be displayed
merged, non_merged = randomisePatterns()
```

## Exceptions

- The `randomisePatterns` function assumes that the LED display is represented as a rectangular grid of LEDs with a width of `board_width` and a height of `board_height`. If the LED display is represented differently, the `randomisePatterns` function should be modified accordingly.

- The `randomisePatterns` function assumes that the function calls of the patterns are the same as the function names in the `precomputations` section.
