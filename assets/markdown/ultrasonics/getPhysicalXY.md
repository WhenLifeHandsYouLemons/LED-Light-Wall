# getPhysicalXY function

## Overview

The `getPhysicalXY` function is a Python function that takes distance readings from ultrasonic sensors and returns the physical X and Y coordinates of an object on a screen. The distances are given in meters from the bottom-left corner of the screen.

## Function Signature

```py
def getPhysicalXY(s_1: float,
                  s_2: float,
                  s_3: float,
                  s_4: float) -> Tuple[float, float]:
    pass
```

## Parameters

- `s_1` = `(float)`: The distance reading from the first sensor measuring the X-axis.
- `s_2` = `(float)`: The distance reading from the second sensor measuring the Y-axis.
- `s_3` = `(float)`: The distance reading from the third sensor measuring the Y-axis.
- `s_4` = `(float)`: The distance reading from the fourth sensor measuring the Y-axis.

## Return Value

- `(float)`: The physical X coordinate of the object on the screen, in meters from the bottom-left corner.
- `(float)`: The physical Y coordinate of the object on the screen, in meters from the bottom-left corner.

## Function Description

The `getPhysicalXY` function takes distance readings from ultrasonic sensors and returns the physical X and Y coordinates of an object on a screen. The function first sets the `x_val` variable to the distance reading from `s_1`.

Next, the function calculates the `y_val` variable by taking the minimum value of the distance readings from `s_2`, `s_3`, and `s_4`, subtracting it from 1, and setting it as the `y_val`. This calculation assumes that the sensors are positioned in such a way that the object being detected is closer to the top of the screen than the bottom.

The function then returns the `x_val` and `y_val` as a tuple.

## Example Usage

```py
# Get the physical X and Y coordinates of an object
x, y = getPhysicalXY(0.5, 0.8, 0.6, 0.7)
print(f"Object detected at X={x}m, Y={y}m")
```

In the example above, we call the `getPhysicalXY` function with example distance readings from the sensors. The function returns the physical X and Y coordinates of the object, which we print to the console.

## Notes

- This function assumes that the distance readings from the ultrasonic sensors are accurate and have been converted to meters. If the distance readings are not accurate or have not been converted to meters, the function may return incorrect physical coordinates.

- The `getPhysicalXY` function does not perform any error checking on the input values or variables used within the function. It is the responsibility of the calling code to ensure that the input values and variables are within the appropriate range and set up correctly for the sensors and screen being used.
