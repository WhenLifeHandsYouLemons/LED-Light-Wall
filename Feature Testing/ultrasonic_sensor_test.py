from gpiozero import DistanceSensor

# https://gpiozero.readthedocs.io/en/stable/api_input.html
# Don't put the GPIO pins to the SDA and SCL on the RPi, it should be on the normal GPIO pins
sensor1 = DistanceSensor(echo=17, trigger=27)
sensor2 = DistanceSensor(echo=22, trigger=5)
while True:
    print(sensor1.distance * 100, "cm &", sensor2.distance * 100, "cm")
