# checkUltrasonics function

## Overview

The `checkUltrasonics` function is a Python function that checks ultrasonic sensors for the presence of objects and displays the position of the object on a screen. This function is useful for applications that require object detection and position tracking, such as autonomous vehicles or robotics.

## Function Signature

```py
def checkUltrasonics() -> None:
    pass
```

## Parameters

This function does not take any parameters.

## Return Value

- `None`: The function does not return anything.

## Function Description

The `checkUltrasonics` function checks ultrasonic sensors for the presence of objects and displays the position of the object on a screen. The function first calls the `objectDetected` function to determine whether an object is present. If an object is detected, the function enters a loop where it repeatedly polls the sensors to ensure that the object is still present. Once it is confirmed that an object is present, the function clears the screen by calling `setAllPixelsColour` with the color black.

Next, the function calls several functions to calculate the X and Y coordinates of the object and map them to the physical dimensions of the screen. These functions include:

- `getPhysicalXY`: calculates the X and Y coordinates of the object based on the sensor readings.
- `getDigitalXY`: maps the physical X and Y coordinates to the digital coordinates of the screen.
- `sensingCompensation`: adjusts the X and Y coordinates to compensate for differences in sensor readings.

Finally, the function calls `displayUltrasonicWave` to display the ultrasonic wave on the screen at the calculated X and Y coordinates.

## Example Usage

```py
# Check for objects and display their position on the screen
checkUltrasonics()
```

In the example above, we call the `checkUltrasonics` function to check for objects and display their position on the screen.

## Notes

- This function assumes that the `objectDetected`, `getPhysicalXY`, `getDigitalXY`, `sensingCompensation`, `setAllPixelsColour`, and `displayUltrasonicWave` functions have been implemented correctly with the appropriate values for the ultrasonic sensors and screen being used. If these functions are not set up correctly, the function may not display object positions correctly or at all.

- The `COLOURS` dictionary should be set up with the appropriate color values for the screen being used. If the color values are not set up correctly, the graphics displayed by the function may not be the expected colors.

- The `checkUltrasonics` function does not perform any error checking on the input values or variables used within the function. It is the responsibility of the calling code to ensure that the input values and variables are within the appropriate range and set up correctly for the sensors and screen being used.

- This function assumes that the ultrasonic sensors have been set up correctly and are functioning properly. If the sensors are not set up correctly or are not functioning properly, the function may not detect objects correctly or at all.