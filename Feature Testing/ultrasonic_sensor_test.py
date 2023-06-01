from gpiozero import DistanceSensor
import time

sensor = DistanceSensor(echo=2, trigger=3)
while True:
    print('Distance: ', sensor.distance * 100)
    # time.sleep(1)
