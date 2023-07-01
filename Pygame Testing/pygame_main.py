"""
Main loop
"""
import sys
import pygame
from datetime import datetime

# Custom imports
from pygame_constants import *
from pygame_utilities import *
from pygame_precomputations import *

# Returns the current time (timezone sensitive) in the format ["hh", "mm", "ss"]
def getTime():
    time = str(datetime.now()).split(" ")[1].split(".")[0]
    time_array = time.split(":")

    return time_array

# Formats the getTime output into "hh:mm:ss"
def formatTime(time_array, hour = False, minute = False, second = False):
    if second == False:
        time_array.pop(2)
    if minute == False:
        time_array.pop(1)
    if hour == False:
        time_array.pop(0)

    time = ":".join(time_array)

    return time

# Reset board
setAllPixelsColour(COLOURS["Black"])

print("\nStarting display.")

while RUNNING_WINDOW == True:
    this_time = formatTime(getTime(), hour=True, minute=True, second=True)
    print(f"\nCurrent time: {this_time}")

    clock.tick(60)

    print("\nCalculating waves...")
    merged, non_merged = randomisePatterns()

    print("Displaying waves.")
    #! Remember to remove the delay of 0 or change it to 0.05
    displayRandomPatterns(merged, non_merged, 0)

    setAllPixelsColour(COLOURS["Black"])

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING_WINDOW = False
            pygame.quit()

sys.exit()
