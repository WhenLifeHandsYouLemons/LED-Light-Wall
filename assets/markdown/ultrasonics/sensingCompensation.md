# sensingCompensation function

## Overview

The `sensingCompensation` function is a Python function that takes physical X and Y coordinates of an object on a screen and compensates for sensing inaccuracies. The function returns compensated X and Y coordinates.

## Function Signature

```py
def sensingCompensation(x_val: float,
                        y_val: float) -> Tuple[float, float]:
    pass
```

## Parameters

- `x_val` = `(float)`: The physical X coordinate of the object on the screen, in meters from the bottom-left corner.
- `y_val` = `(float)`: The physical Y coordinate of the object on the screen, in meters from the bottom-left corner.

## Return Value

- `(float)`: The compensated X coordinate of the object on the screen, in meters from the bottom-left corner.
- `(float)`: The compensated Y coordinate of the object on the screen, in meters from the bottom-left corner.

## Function Description

The `sensingCompensation` function takes physical X and Y coordinates of an object on a screen and compensates for sensing inaccuracies. The function first sets the `max_change` variable to 3. This value represents the maximum amount of compensation that the function can apply to the `y_val` variable.

Next, the function checks whether the `y_val` variable is greater than or equal to `max_change`. If it is, the function calculates a compensation value based on the equation `(-0.1 * y_val) + 3`. The function rounds this compensation value up to the nearest integer using the `math.ceil` function and subtracts it from the `y_val` variable to get the compensated `y_val`.

The function then returns the `x_val` and compensated `y_val` variables as a tuple.

## Example Usage

```py
# Get the compensated X and Y coordinates of an object
x, y = sensingCompensation(0.5, 0.7)
print(f"Compensated coordinates: X={x}, Y={y}")
```

In the example above, we call the `sensingCompensation` function with example physical X and Y coordinates of an object. The function returns the compensated X and Y coordinates of the object, which we print to the console.

## Notes

- This function assumes that the physical X and Y coordinates have been accurately measured and are in meters from the bottom-left corner of the screen. If the physical coordinates are not accurate or are measured using a different coordinate system, the function may not compensate accurately.

- The `sensingCompensation` function applies compensation only to the `y_val` variable and only if it is greater than or equal to `max_change`. The compensation value is calculated based on a fixed equation and rounded up to the nearest integer. These values may need to be adjusted based on the specific screen and sensing setup being used.