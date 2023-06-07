from gpiozero import DistanceSensor
import matplotlib as plt
import time

# https://gpiozero.readthedocs.io/en/stable/api_input.html
# Don't put the GPIO pins to the SDA and SCL on the RPi, it should be on the normal GPIO pins
sensor1 = DistanceSensor(echo=17, trigger=27)
sensor2 = DistanceSensor(echo=22, trigger=5)
# All data is in cm
sensor1_data = []
sensor2_data = []

# Collect data for 10 seconds
start_time = time.time()
end_time = 0
DURATION = 10

while end_time - start_time < DURATION:
    sensor1_data.append(round(sensor1.distance * 100, 0))
    sensor2_data.append(round(sensor2.distance * 100, 0))
    # print(sensor1.distance * 100, "cm &", sensor2.distance * 100, "cm")
    end_time = time.time()

# Display data in matplotlib
DEBUG = True
if DEBUG:
    plt.plot(sensor1_data, sensor2_data, "ro")
    plt.title("Field of View of the Ultrasonic Sensors")
    plt.grid(True)
    plt.xlim([0, 100])
    plt.ylim([0, 100])
    plt.ylabel("y-axis sensors (cm)")
    plt.xlabel("x-axis sensors (cm)")
    plt.show()
