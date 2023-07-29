# displayUltrasonicWave function

## Overview

The `displayUltrasonicWave` function is a Python function that displays a wave on the board at the inputted XY coordinates. The function takes an X and Y coordinate, generates a circular wave, and displays it on the board.

## Function Signature

```py
def displayUltrasonicWave(x_val: float, y_val: float, delay: float = 0) -> None:
    pass
```

## Parameters

- `x_val` = `(float)`: The X coordinate of the wave on the board.
- `y_val` = `(float)`: The Y coordinate of the wave on the board.
- `delay` = `(float)`: The delay time in seconds between each frame of the wave. The default is 0.

## Return Value

- None: This functions doesn't return anything.

## Function Description

The `displayUltrasonicWave` function takes an X and Y coordinate of an object on a screen, generates a circular wave using the `precomputations.precomputeCircularWave` function, and displays it on the board using the `setPixelsColour` function. The function first calls the `precomputations.precomputeCircularWave` function with the `x_val`, `y_val`, and a radius of 10. This generates a circular wave based on the input coordinates.

Next, the function calls the `precomputations.precomputeColours` function with the generated circular wave, a green color, a black color, and a thickness of 5. This precomputes the colors for each LED in the wave.

Then, the function iterates over each tick of the wave and each LED in the tick. For each LED, the function converts the color values to integers to avoid any float errors and sets the color of the LED using the `setPixelsColour` function.

The function then displays the wave on the board using the `pixels.show()` function and sleeps for a delay time specified by the `delay` parameter.

## Example Usage

```py
# Display an ultrasonic wave on the board
displayUltrasonicWave(0.5, 0.7, 0.1)
```

In the example above, we call the `displayUltrasonicWave` function with example values of `x_val` and `y_val`. The function displays an ultrasonic wave on the board with a delay of 0.1 seconds between each frame.

## Notes

- This function assumes that the `pixels` object and `COLOURS` dictionary have been defined and initialized correctly. If they have not, the function may not display the wave correctly.

- The `displayUltrasonicWave` function generates a circular wave based on the input X and Y coordinates and displays it on the board. The thickness of the wave and the colors used for the wave are fixed and may need to be adjusted based on the specific board and display setup being used.