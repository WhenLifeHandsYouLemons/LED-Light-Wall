from datetime import datetime
import time

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

on_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
on_time_range = [[8, 0, 0], [16, 30, 0]]


# Startup information
print(f"\n{formatTime(getTime(), hour=True, minute=True, second=True, ampm=True)}")
print(getDay()[0])

# Main loop
while True:
    # Get today's day
    this_day = getDay()
    run_check = False

    # While it's a weekday
    while this_day[0] in on_days:
        # Get current time
        this_time = getTime()
        print(f"\nCurrent time: {formatTime(this_time, hour=True, minute=True, second=True, ampm=True)}")

        # Checks if current time and day is within valid range
        run_check = False
        if (this_day[0] in on_days) and ((this_time[0] > on_time_range[0][0] and this_time[0] < on_time_range[1][0]) or ((this_time[0] == on_time_range[0][0]) and ((this_time[1] > on_time_range[0][1]) or ((this_time[1] == on_time_range[0][1]) and (this_time[2] >= on_time_range[0][2])))) or ((this_time[0] == on_time_range[1][0]) and ((this_time[1] < on_time_range[1][1]) or ((this_time[1] == on_time_range[1][1]) and (this_time[2] < on_time_range[1][2]))))):
            run_check = True

        # If it's supposed to be displaying
        if run_check == True:
            # Display anything in here
            pass
        else:
            time.sleep(60)

    # While it's a weekend
    while this_day[0] not in on_days:
        this_day = getDay()
        print(f"\nStopped for 24 hours because today is {this_day[0]}.\nWait until one of these days: {on_days}.")

        # Don't do anything for 7h59m59s
        # I chose that specific number so that there's enough time for it to
        # recheck the day and go into normal operation by 8am.
        time.sleep(28799)
