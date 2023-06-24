# changeWaveSpeed function

## Overview

The `changeWaveSpeed` function takes a wave array that includes color information and changes its speed based on the given ratio. This can be used to slow down or speed up the wave animation. If the ratio is less than 1, the function duplicates each tick in the wave array to slow down the wave. If the ratio is greater than 1, the function removes ticks from the wave array to speed up the wave.

## Function Signature

```py
def changeWaveSpeed(wave_array: List[List[List[int]]], ratio: float = 1) -> List[List[List[int]]]:
    pass
```

## Parameters

- `wave_array` = `List[List[List[int]]]`: A three-dimensional list representing the LED coordinates and color values for each tick in the wave animation. Each top-level item in the list represents a tick, and each item in the second-level list represents an LED that should be illuminated for that tick. The third-level list contains the x and y coordinates of the LED, as well as its RGB color values.

- `ratio` = `float`: A float value representing the ratio by which the wave speed should be changed. If the ratio is less than 1, the wave speed will be slowed down. If the ratio is greater than 1, the wave speed will be sped up. The default value is 1, which means that the wave speed will not be changed.

## Return Value

- `List[List[List[int]]]`: A three-dimensional list representing the new wave array with the changed speed. Each top-level item in the list represents a tick, and each item in the second-level list represents an LED that should be illuminated for that tick. The third-level list contains the x and y coordinates of the LED, as well as its RGB color values.

## Function Description

The `changeWaveSpeed` function takes a wave array that includes color information and changes its speed based on the given ratio.

If the ratio is less than 0, the function raises a `ValueError` with a message indicating that the ratio is out of bounds.

If the ratio is less than 1, the function duplicates each tick in the wave array by a number of times equal to the inverse of the ratio. For example, if the ratio is 0.5, each tick in the wave array will be duplicated twice. The duplicated ticks are added to a new wave array.

If the ratio is greater than 1, the function removes ticks from the wave array by a number of times equal to the ratio minus 1. For example, if the ratio is 2, every other tick in the wave array will be removed. The remaining ticks are added to a new wave array.

The function returns the new wave array with the changed speed.

## Example Usage

```py
# Change wave speed by slowing it down
new_wave_array = changeWaveSpeed(wave_array, 0.5)

# Change wave speed by speeding it up
new_wave_array = changeWaveSpeed(wave_array, 2.0)
```

In the examples above, we call the `changeWaveSpeed` function to change the speed of a wave array by slowing it down or speeding it up.

## Exceptions

- The `changeWaveSpeed` function assumes that the LED coordinates in the wave array are represented as a list of two integers. If the LED coordinates are represented differently, the function should be modified accordingly.

- The `changeWaveSpeed` function assumes that the wave array has at least one tick. If the wave array is empty, the function may raise an error.

- The `changeWaveSpeed` function assumes that the ratio is a float value. If the ratio is represented differently, the function should be modified accordingly.

- The `changeWaveSpeed` function assumes that the ratio is not negative. If the ratio is negative, the function raises a `ValueError` with a message indicating that the ratio is out of bounds.