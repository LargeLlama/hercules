def militaryTime(time):
    AMorPM = time[len(time)-2:len(time)]
    hour = time[0:2]
    if (AMorPM == "PM" or AMorPM =="AM"):
        hour = int(hour) + 12
        return str(hour) + time[2:len(time)-2]
    else:
        return time


