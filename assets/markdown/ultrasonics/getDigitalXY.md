# getDigitalXY function

## Overview

The `getDigitalXY` function is a Python function that takes physical X and Y coordinates of an object on a screen and returns digital X and Y coordinates that can be displayed on the board.

## Function Signature

```py
def getDigitalXY(x_val: float,
                 y_val: float) -> Tuple[int, int]:
    pass
```

## Parameters

- `x_val` = `(float)`: The physical X coordinate of the object on the screen, in meters from the bottom-left corner.
- `y_val` = `(float)`: The physical Y coordinate of the object on the screen, in meters from the bottom-left corner.

## Return Value

- `(int)`: The digital X coordinate of the object on the screen, starting from the bottom-left corner.
- `(int)`: The digital Y coordinate of the object on the screen, starting from the bottom-left corner.

## Function Description

The `getDigitalXY` function takes physical X and Y coordinates of an object on a screen and returns digital X and Y coordinates that can be displayed on the board. The function first rounds the `x_val` and `y_val` variables to the nearest centimeter using the `round` function.

Next, the function maps the `x_val` and `y_val` values to the digital scale used by the board. The function multiplies the `x_val` by 26 and the `y_val` by 20 to remap them to the digital scale. These values are chosen based on the assumed size of the screen and the number of pixels used to represent it on the board.

Lastly, the function rounds the `dig_x` and `dig_y` values to the nearest integer using the `round` function and converts them to integers using the `int` function. The function then returns the `dig_x` and `dig_y` values as a tuple.

## Example Usage

```py
# Get the digital X and Y coordinates of an object
x, y = getDigitalXY(0.5, 0.7)
print(f"Object detected at X={x}, Y={y}")
```

In the example above, we call the `getDigitalXY` function with example physical X and Y coordinates of an object. The function returns the digital X and Y coordinates of the object, which we print to the console.

## Notes

- This function assumes that the physical X and Y coordinates have been accurately measured and are in meters from the bottom-left corner of the screen. If the physical coordinates are not accurate or are measured using a different coordinate system, the function may return incorrect digital coordinates.

- The `getDigitalXY` function uses fixed values to map the physical coordinates to the digital scale used by the board. These values may need to be adjusted based on the specific screen and board being used.