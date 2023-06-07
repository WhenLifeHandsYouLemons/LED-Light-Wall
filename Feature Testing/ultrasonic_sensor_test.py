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

# Collect data for 10 seconds
start_time = time.time()
end_time = 0
DURATION = 10

while end_time - start_time < DURATION:
    s1 = sensor1.distance
    s2 = sensor2.distance
    s3 = sensor3.distance
    print(s1, s2)
    # Calculate change in previous and current value
    s1_dydx = sensor1_data[-1] - s1
    s2_dydx = sensor2_data[-1] - s2
    s3_dydx = sensor3_data[-1] - s3
    if s1_dydx < 0:
        s1 *= -1
    if s2_dydx < 0:
        s2_dydx *= -1
    # Remove if outside allowed range
    if s1 < 1 and s2 < 1 and s1_dydx < 0.1 and s2_dydx < 0.1 and s3_dydx < 0.1:
        sensor1_data.append(round(s1 * 100, 2))
        sensor2_data.append(round(s2 * 100, 2))
        sensor3_data.append(round(s3 * 100, 2))
    # print(sensor1.distance * 100, "cm &", sensor2.distance * 100, "cm")
    end_time = time.time()

# Display data in matplotlib
print(sensor1_data, sensor2_data, sensor3_data)
DEBUG = True
if DEBUG:
    plt.plot(sensor1_data, sensor2_data)
    plt.title("Field of View of the Ultrasonic Sensors")
    plt.grid(True)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.ylabel("y-axis sensors (cm)")
    plt.xlabel("x-axis sensors (cm)")
    plt.show()
