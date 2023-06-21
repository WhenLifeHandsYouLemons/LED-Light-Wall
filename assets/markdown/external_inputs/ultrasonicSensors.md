# ultrasonicSensors function

## Overview

The `ultrasonicSensors` function reads data from four ultrasonic sensors and calculates the physical position of an object detected by the sensors. It then maps the physical position to the corresponding LED position on a display and displays a wave of light on the LED display.

## Function Signature

```py
def ultrasonicSensors(x: float,
                      y: float) -> Tuple[float, float]:
    pass
```

## Parameters

- `x` = `float`: A float value representing the previous x position of the detected object.
- `y` = `float`: A float value representing the previous y position of the detected object.

## Return Value

- `Tuple[float, float]`: A tuple containing the x and y position of the detected object.

## Function Description

The `ultrasonicSensors` function reads data from four ultrasonic sensors and calculates the physical position of an object detected by the sensors. It then maps the physical position to the corresponding LED position on a display and displays a wave of light on the LED display.

The function starts by storing the previous x and y position values in the `p_x` and `p_y` variables.

It then reads data from four ultrasonic sensors using the `distance` attribute of each sensor object. If any of the sensors detect an object, the function proceeds to calculate the physical position of the detected object.

The physical position is calculated by first normalizing the distance values of the sensors to a range of 0 to 1, where a distance of 1 represents the maximum detection range of the sensor. The x position of the object is then set to the normalized distance value of the first sensor. The y position of the object is set to the minimum normalized distance value of the remaining sensors.

The function then calculates the change in the x and y position values from the previous position values and maps the physical position to the corresponding LED position on the display. The LED position is calculated by multiplying the normalized x and y position values by the total number of LEDs in the x and y directions, respectively, and rounding the result to the nearest integer.

The function then compensates for sensing inaccuracies by adjusting the LED position based on the value of the normalized y position.

Finally, the function displays a wave of light on the LED display using the `displayWave` function, which takes as input a precomputed wave of colors and displays it on the LED display.

## Example Usage

```py
# Initialize the x and y position values
x, y = 0, 0

# Continuously read data from the ultrasonic sensors and display a wave of light on the LED display
while True:
    x, y = ultrasonicSensors(x, y)
```

In the example above, we continuously read data from the ultrasonic sensors and display a wave of light on the LED display using the `ultrasonicSensors` function.

## Exceptions

- The `ultrasonicSensors` function assumes that the ultrasonic sensors are defined properly and can be used to read distance data. If the sensors are not defined properly, the function may not work as expected.

- The `ultrasonicSensors` function assumes that the `displayWave` function is defined properly and can be used to display a wave of light on the LED display. If this function is not defined properly, the function may not work as expected.

- The `ultrasonicSensors` function may not work as expected if there are no objects detected by the sensors or if the sensors detect objects outside their maximum detection range. In this case, the function may not display a wave of light on the LED display or may display an incorrect wave of light.

- The pin wirings of all the ultrasonic sensors are customised for our project. If this doesn't work for you, you can try changing the pin wiring.
  - You can initialise an ultrasonic sensor by writing this line of code: `sensor1 = DistanceSensor(echo=17, trigger=27)`.
  - You can replace 17 and 27 to different pin numbers.
