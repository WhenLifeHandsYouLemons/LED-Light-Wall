from datetime import datetime
import time

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

# Returns a string of today's day
def getDay():
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = datetime.weekday(datetime.now())
    return days[day]

print(getTime())
print(getDay())

on_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
on_time_ranges = [[["08", "00", "00"], []]]

while True:
    # Get today's day
    this_day = getDay()

    # While it is a weekday
    while this_day in on_days:
        # Get current time
        this_time = getTime()
        print(this_time)

        # Get the current day at 8am every day
        if this_time == ["08", "00", "00"]:
            this_day = getDay()

        # If the time is in the valid time range
            # Do stuff

    # If it's a weekend
    while this_day not in on_days:
        this_day = getDay()

        # Don't do anything for 23h59m59s
        # I chose that specific number so that there's enough time for it to
        # recheck the day and go into normal operation by 8am.
        time.sleep(86399)
