"""
Raspberry Pi Temporary Display
"""
import time

# Custom imports
from rpi import *
from utilities import *
from precomputations import *
from graphics import *

# Reset board
setAllPixelsColour(pixels, COLOURS["Black"])

print("Calculating waves, please wait...")

# Compute test waves
merge1 = []
merge1.append(precomputeColours(precomputeRain(10), COLOURS["Dark Blue"], COLOURS["Black"], 7))
merge1.append(precomputeColours(precomputeRain(11), COLOURS["Dark Blue"], COLOURS["Black"], 7))
merge1.append(precomputeColours(precomputeRain(16), COLOURS["Dark Blue"], COLOURS["Black"], 7))
merge1.append(precomputeColours(precomputeRain(5), COLOURS["Dark Blue"], COLOURS["Black"], 7))
merge1.append(precomputeColours(precomputeRain(23), COLOURS["Dark Blue"], COLOURS["Black"], 7))
merge1.append(precomputeColours(precomputeRain(1), COLOURS["Dark Blue"], COLOURS["Black"], 7))
merge1.append(precomputeColours(precomputeRain(29), COLOURS["Dark Blue"], COLOURS["Black"], 7))
merged1 = mergeWaves(merge1, [0, 3, 4, 10, 2, 7, 0])

merge2 = []
merge2.append(precomputeColours(precomputeCircularWave(15, 10, 9), COLOURS["Red"], COLOURS["Black"], 3))
merge2.append(precomputeColours(precomputeWave(1, 29), COLOURS["Red Orange"], COLOURS["Black"], 6))
merge2.append(precomputeColours(precomputeRipple(10, 6, 10), COLOURS["Lime"], COLOURS["Black"], 4))
merged2 = mergeWaves(merge2, [5, 0, 7])

print("Starting display.")

while True:
    pixels, pixel_framebuf = changeBrightness(1)

    setAllPixelsColour(pixels, COLOURS["Black"])
    displayWave(merged1, 0.05)

    setAllPixelsColour(pixels, COLOURS["Black"])
    displayWave(merged2, 0.08)

    setAllPixelsColour(pixels, COLOURS["Black"])
    drawText("CLASS", COLOURS["Dark Blue"], 0, 2)
    drawText("2023", COLOURS["Purple"], 4, 11)
    time.sleep(5)

    setAllPixelsColour(pixels, COLOURS["Black"])
    drawText("LED", COLOURS["Lime"], 7, 2)
    drawText("WALL", COLOURS["Yellow"], 4, 11)
    time.sleep(5)
