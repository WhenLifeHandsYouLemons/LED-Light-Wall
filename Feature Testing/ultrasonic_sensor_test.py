import math
from gpiozero import DistanceSensor
import matplotlib.pyplot as plt
import time

# https://gpiozero.readthedocs.io/en/stable/api_input.html
# Don't put the GPIO pins to the SDA and SCL on the RPi, it should be on the normal GPIO pins
sensor1 = DistanceSensor(echo=17, trigger=27)
sensor2 = DistanceSensor(echo=22, trigger=23)
sensor3 = DistanceSensor(echo=26, trigger=6)
sensor4 = DistanceSensor(echo=5, trigger=16)

amount = 0
avg = 0
while amount < 10:
    # All data is in cm
    x_axis = []
    y_axis = []

    # Collect data for 10 seconds
    start_time = time.time()
    end_time = 0
    DURATION = 1
    MAX_CHANGE = 0.25

    while end_time - start_time < DURATION:
        # Get data from the sensors
        # s1 is on the short edge (might need to add an extra one here)
        s1 = sensor1.distance
        # s2, s3, s4 are on the long edge
        s2 = sensor2.distance
        s3 = sensor3.distance
        s4 = sensor4.distance

        # Check which sensor is detecting the object
        x = s1
        if s2 > 0.7:
            s2 = 1
        if s3 > 0.7:
            s3 = 1
        if s4 > 0.7:
            s4 = 1

        if s2 < s3 and s2 < s4:
            y = s2
        elif s3 < s2 and s3 < s4:
            y = s3
        else:
            y = s4
        y = 1 - y

        # Weird bug but the sensor data only stores in the array if you print it out
        print(x, y)

        # Calculate change in previous and current value
        if len(y_axis) > 0:
            dx = math.fabs(x - x_axis[-1])
            dy = math.fabs(y - y_axis[-1])
        else:
            dx, dy = 0, 0
            x = 0
            y = 0

        # Remove if outside allowed range
        if s1 < 1 and (s2 < 1 or s3 < 1 or s4 < 1) and dx < MAX_CHANGE and dy < MAX_CHANGE:
            x_axis.append(round(x, 4))
            y_axis.append(round(y, 4))
        elif len(y_axis) > 0:
            x_axis.append(x_axis[-1])
            y_axis.append(y_axis[-1])
        else:
            x_axis.append(0)
            y_axis.append(0)

        end_time = time.time()

    avg += len(x_axis)
    amount += 1

print(avg / (amount + 1))

# Display data in matplotlib
i = 0
while i < len(x_axis):
    x_axis[i] *= 100
    y_axis[i] *= 100
    i += 1

DEBUG = False
if DEBUG:
    print(x_axis, y_axis)
    plt.plot(x_axis, y_axis, "ro")
    plt.title("Field of View of the Ultrasonic Sensors")
    plt.grid(True)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.ylabel("y-axis sensors (cm)")
    plt.xlabel("x-axis sensors (cm)")
    plt.show()
