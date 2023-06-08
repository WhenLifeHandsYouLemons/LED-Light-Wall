import math
from gpiozero import DistanceSensor
import matplotlib.pyplot as plt
import time

# https://gpiozero.readthedocs.io/en/stable/api_input.html
# Don't put the GPIO pins to the SDA and SCL on the RPi, it should be on the normal GPIO pins
sensor1 = DistanceSensor(echo=17, trigger=27)
sensor2 = DistanceSensor(echo=22, trigger=23)
sensor3 = DistanceSensor(echo=26, trigger=6)
# All data is in cm
sensor1_data = []
sensor2_data = []
sensor3_data = []
x_axis = []
y_axis = []


# Collect data for 10 seconds
start_time = time.time()
end_time = 0
DURATION = 10

while end_time - start_time < DURATION:
    # Get data from the sensors
    s1 = sensor1.distance
    s2 = sensor2.distance
    s3 = sensor3.distance

    # Save to a variable depending on which sensor is detecting the object
    x = s1
    if s2 > s3:
        y = s3
    else:
        y = s2
    # Weird bug but the sensor data only stores in the array if you print it out
    print(x, y)

    # Calculate change in previous and current value
    if len(sensor1_data) > 0:
        s1_dydx = math.fabs(sensor1_data[-1] - s1)
        s2_dydx = math.fabs(sensor2_data[-1] - s2)
        s3_dydx = math.fabs(sensor3_data[-1] - s3)
    else:
        s1_dydx, s2_dydx, s3_dydx = 0, 0, 0

    # Remove if outside allowed range
    if s1 < 1 and (s2 < 1 or s3 < 1) and s1_dydx < 0.1 and s2_dydx < 0.1 and s3_dydx < 0.1:
        sensor1_data.append(round(s1 * 100, 2))
        sensor2_data.append(round(s2 * 100, 2))
        sensor3_data.append(round(s3 * 100, 2))
        x_axis.append(round(x * 100, 2))
        y_axis.append(round(y * 100, 2))

    end_time = time.time()

# Display data in matplotlib
print(x_axis, y_axis)

DEBUG = True
if DEBUG:
    plt.plot(x_axis, y_axis)
    plt.title("Field of View of the Ultrasonic Sensors")
    plt.grid(True)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.ylabel("y-axis sensors (cm)")
    plt.xlabel("x-axis sensors (cm)")
    plt.show()
