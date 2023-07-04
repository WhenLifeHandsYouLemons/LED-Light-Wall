"""
Main loop
"""
import sys
import pygame
from datetime import datetime
import time

# Custom imports
from pygame_constants import *
from pygame_utilities import *
from pygame_precomputations import *


# Returns the current time (timezone sensitive) in the format [hour, minute, second]
# where each value is an integer
def getTime():
    time = str(datetime.now()).split(" ")[1].split(".")[0]
    time_array = time.split(":")

    for i in range(len(time_array)):
        time_array[i] = int(time_array[i])

    return time_array

# Formats the getTime output into "hh:mm:ss"
def formatTime(time_array, hour = False, minute = False, second = False, ampm = False):
    # Don't alter original data
    time_array = time_array.copy()

    time_value = ""
    # Remove any values that user doesn't want
    if second == False:
        time_array.pop(2)
    if minute == False:
        time_array.pop(1)
    if hour == False:
        time_array.pop(0)
    elif ampm == True:  # If user wants it in 24-hour time
        if time_array[0] >= 12:
            time_array[0] -= 12
            time_value = "PM"
        else:
            time_value = "AM"

        if time_array[0] == 0:
            time_array[0] = 12

    for i in range(len(time_array)):
        time_array[i] = str(time_array[i])

    time = f"{':'.join(time_array)} {time_value}"

    return time

# Returns a string of today's day
def getDay():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = datetime.weekday(datetime.now())
    return days[day], day

# Allowed time and days
on_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# Uses 24-hour time format
on_time_range = [[8, 0, 0], [16, 30, 0]]

# Reset board
setAllPixelsColour(COLOURS["Black"])

# Startup information
print("\nStarting display.")
print(f"\n{formatTime(getTime(), hour=True, minute=True, second=True, ampm=True)}")
print(getDay()[0])

# Main loop
while RUNNING_WINDOW:
    clock.tick(60)

    # Get today's day
    this_day = getDay()
    run_check = False

    # While it's a weekday
    while this_day[0] in on_days and RUNNING_WINDOW:
        # Get current time
        this_time = getTime()
        print(f"\nCurrent time: {formatTime(this_time, hour=True, minute=True, second=True, ampm=True)}")

        # Checks if current time and day is within valid range
        run_check = False
        # I've shortened it to hopefully make it check faster
        if (this_day[0] in on_days) and ((this_time[0] > on_time_range[0][0] and this_time[0] < on_time_range[1][0]) or ((this_time[0] == on_time_range[0][0]) and ((this_time[1] > on_time_range[0][1]) or ((this_time[1] == on_time_range[0][1]) and (this_time[2] >= on_time_range[0][2])))) or ((this_time[0] == on_time_range[1][0]) and ((this_time[1] < on_time_range[1][1]) or ((this_time[1] == on_time_range[1][1]) and (this_time[2] < on_time_range[1][2]))))):
            run_check = True

        # If it's supposed to be displaying
        if run_check == True:
            # Do stuff
            print("\nCalculating waves...")
            merged, non_merged = randomisePatterns()

            print("Displaying waves.")
            displayRandomPatterns(merged, non_merged, 0.05)

            setAllPixelsColour(COLOURS["Black"])

            pygame.display.update()
        else:
            # Wait for 5 minutes before rechecking the day and time
            time.sleep(60 * 5)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUNNING_WINDOW = False
                pygame.quit()

    # While it's a weekend
    while this_day[0] not in on_days and RUNNING_WINDOW:
        print(f"\nStopped for 8 hours because today is {this_day[0]}.\nWait until one of these days: {on_days}.")

        # Don't do anything for the minimum amount of time possible - 10 seconds
        # I choose the number so that there's enough time for it to
        # recheck the day and go into normal operation by it's specified on time.
        time.sleep((on_time_range[0][0] * 60 * 60) + (on_time_range[0][1] * 60) + (on_time_range[0][2]) - 10)

        # Recheck the day after sleeping
        # This fixes an issue where it would get the day but finish the loop
        # once more before exiting, which meant it sleeps for 8 hours on Monday
        this_day = getDay()

sys.exit()
