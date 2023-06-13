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
x_axis = []
y_axis = []


# Collect data for 10 seconds
start_time = time.time()
end_time = 0
DURATION = 3

initial = 0
while end_time - start_time < DURATION:
    # Get data from the sensors
    s1 = sensor1.distance
    s2 = sensor2.distance
    s3 = sensor3.distance

    # Check which sensor is detecting the object
    x = s1
    if s2 > s3:
        if s2 - s3 < 10:
            x = (s3 + (s2 - s3)/2)
        else:
            y = s3
    else:
        if s3 - s2 < 10:
            x = (s2 + (s3 - s2)/2)
        else:
            y = s2
    # Weird bug but the sensor data only stores in the array if you print it out
    # print(x, y)

    # Calculate change in previous and current value
    if len(y_axis) > 0:
        dx = math.fabs(x - x_axis[-1])
        dy = math.fabs(y - y_axis[-1])
    else:
        dx, dy = 0, 0
        x = 0
        y = 0

    print(x, y, dx, dy)

    # Remove if outside allowed range
    add = True
    #  and dx < 0.5 and dy < 0.5
    if len(y_axis) > 0:
        if x == x_axis[-1] and y == y_axis[-1]:
            add = False

    if initial < 10:
        add = True
        initial += 1

    if s1 < 1 and (s2 < 1 or s3 < 1) and (add or (dx < 0.25 and dy < 0.25)):
        x_axis.append(round(x, 4))
        y_axis.append(round(y, 4))
    else:
    # elif (not add or not (dx < 0.25 and dy < 0.25)):
        x_axis.append(x_axis[-1])
        y_axis.append(y_axis[-1])

    end_time = time.time()

# Display data in matplotlib
i = 0
while i < len(x_axis):
    x_axis[i] *= 100
    y_axis[i] *= 100
    i += 1
print(x_axis, y_axis)

DEBUG = True
if DEBUG:
    plt.plot(x_axis, y_axis, "ro")
    plt.title("Field of View of the Ultrasonic Sensors")
    plt.grid(True)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.ylabel("y-axis sensors (cm)")
    plt.xlabel("x-axis sensors (cm)")
    plt.show()