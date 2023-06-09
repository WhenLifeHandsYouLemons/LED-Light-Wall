"""
For Ultrasonics
"""
import time
import math
from gpiozero import DistanceSensor

# Custom imports
from rpi import *
from utilities import *
import precomputations

# Initialise sensors
# https://gpiozero.readthedocs.io/en/stable/api_input.html
# Don't put the GPIO pins to the SDA and SCL on the RPi, it should be on the normal GPIO pins
sensor1 = DistanceSensor(echo=17, trigger=27)
sensor2 = DistanceSensor(echo=22, trigger=24)
sensor3 = DistanceSensor(echo=26, trigger=6)
sensor4 = DistanceSensor(echo=5, trigger=16)

# Runs all ultrasonic code required in a simple function to be called when needed
def checkUltrasonics():
    detected, s1, s2, s3, s4 = objectDetected()

    # While there's an object in the way
    while detected == True:
        # Poll for new sensor data
        detected, s1, s2, s3, s4 = objectDetected()

        # Recheck if there's still an object and the sensor just didn't pick it up
        if detected == False:
            time.sleep(0.5)
            detected, s1, s2, s3, s4 = objectDetected()

        # Clear board
        setAllPixelsColour(pixels, COLOURS["Black"])

        # Get x and y coordinates of object and map to board
        x, y = getPhysicalXY(s1, s2, s3, s4)
        x, y = getDigitalXY(x, y)
        x, y = sensingCompensation(x, y)

        # Display the wave
        displayUltrasonicWave(x, y)

# Returns True or False if there is an object detected on the board
def objectDetected():
    # s1 is measuring x-axis
    sen1 = sensor1.distance
    # s2, s3, s4 are measuring y-axis
    sen2 = sensor2.distance
    sen3 = sensor3.distance
    sen4 = sensor4.distance

    if sen2 >= 0.7:
        sen2 = 1
    if sen3 >= 0.7:
        sen3 = 1
    if sen4 >= 0.7:
        sen4 = 1

    if sen1 < 1 and (sen2 < 0.7 or sen3 < 0.7 or sen4 < 0.7):
        return True, sen1, sen2, sen3, sen4

    return False, sen1, sen2, sen3, sen4

# Returns a physical x and y value from the sensor data given
# The distances are given in metres from the bottom-left corner
def getPhysicalXY(s_1, s_2, s_3, s_4):
    x_val = s_1

    y_values = [s_2, s_3, s_4]
    y_val = 1 - min(y_values)

    return x_val, y_val

# Returns a digital x and y value from the physical values which can be displayed on the board
# The values start from the bottom-left corner
def getDigitalXY(x_val, y_val):
    # Round to nearest centimetre
    dig_x = round(x_val, 4)
    dig_y = round(y_val, 4)

    # Remap to digital scale
    dig_x *= 26
    dig_y *= 20

    # Convert it to discrete integer values to display on the board
    dig_x = int(round(dig_x, 0))
    dig_y = int(round(dig_y, 0))

    return dig_x, dig_y

# Returns compensated coordinate values for sensing inaccuracies
def sensingCompensation(x_val, y_val):
    max_change = 3

    if y_val >= max_change:
        y_val -= math.ceil((-0.1 * y_val) + 3)

    return x_val, y_val

# Displays a wave on the board at the inputted xy coordinates
def displayUltrasonicWave(x_val, y_val, delay = 0):
    wave = precomputations.precomputeColours(precomputations.precomputeCircularWave(x_val, y_val, 10), COLOURS["Green"], COLOURS["Black"], 5)

    for tick in wave:
        for LED in tick:
            # Change all colour values to integers to stop any float errors
            LED[2][0] = int(LED[2][0])
            LED[2][1] = int(LED[2][1])
            LED[2][2] = int(LED[2][2])
            setPixelsColour(pixels, LED[2], getLED(LED[0], LED[1]))

        pixels.show()
        time.sleep(delay)
