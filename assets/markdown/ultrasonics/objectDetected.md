# objectDetected function

## Overview

The `objectDetected` function is a Python function that uses ultrasonic sensors to detect whether an object is present on a screen. The function returns a boolean value indicating whether an object is present, as well as the distance readings from the sensors.

## Function Signature

```py
def objectDetected() -> Tuple[bool, float, float, float, float]:
    pass
```

## Parameters

This function does not take any parameters.

## Return Value

- `(bool)`: A boolean value indicating whether an object is present on the screen. Returns `True` if an object is present, and `False` otherwise.
- `s1` = `(float)`: The distance reading from the first sensor measuring the X-axis.
- `s2` = `(float)`: The distance reading from the second sensor measuring the Y-axis.
- `s3` = `(float)`: The distance reading from the third sensor measuring the Y-axis.
- `s4` = `(float)`: The distance reading from the fourth sensor measuring the Y-axis.

## Function Description

The `objectDetected` function uses ultrasonic sensors to detect whether an object is present on a screen. The function first reads the distance values from the four sensors (s1, s2, s3, s4) using the `distance` attribute of each sensor object. The function then checks whether there is an object present by checking the distance values against certain thresholds.

If the distance value from `s1` is less than 1 and at least one of the `s2`, `s3`, or `s4` distance values is less than 0.7, the function returns `True` to indicate that an object is present. Otherwise, the function returns `False`.

The function also adjusts the distance values for `s2`, `s3`, and `s4` to ensure that they are between 0 and 1. This is done to simplify the object detection logic.

## Example Usage

```py
# Check whether an object is detected and get sensor readings
while True:
    detected, s1, s2, s3, s4 = objectDetected()

    if detected:
        print("Object detected!")
    else:
        print("No object detected.")
```

In the example above, we call the `objectDetected` function to check whether an object is present on the screen and retrieve the sensor readings. If an object is detected, we print a message indicating that an object has been detected. Otherwise, we print a message indicating that no object has been detected.

## Notes

- This function assumes that the ultrasonic sensors have been set up correctly and are functioning properly. If the sensors are not set up correctly or are not functioning properly, the function may not detect objects correctly or at all.

- The distance thresholds used in this function (`1` for `s1` and `0.7` for `s2`, `s3`, and `s4`) may need to be adjusted based on the specific dimensions of the board being used. If the thresholds are set too high or too low, the function may not detect objects correctly or at all.

- The `objectDetected` function does not perform any error checking on the input values or variables used within the function. It is the responsibility of the calling code to ensure that the input values and variables are within the appropriate range and set up correctly for the sensors and screen being used.