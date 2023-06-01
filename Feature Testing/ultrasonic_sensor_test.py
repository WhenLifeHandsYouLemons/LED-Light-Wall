from gpiozero import DistanceSensor

# Don't put the GPIO pins to the SDA and SCL on the RPi, it should be on the normal GPIO pins
sensor = DistanceSensor(echo=17, trigger=27)
while True:
    print(sensor.distance * 100, "cm")
