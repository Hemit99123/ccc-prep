# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# ccc j3 2009
# 31 oct 2024

ottawa_time = int(input())

time_differences = {
    "Victoria": -300,
    "Edmonton": -200,
    "Winnipeg": -100,
    "Toronto": 0,
    "Halifax": 100,
    "St. John's": 130
}

print("{} in Ottawa".format(ottawa_time))

for key, value in time_differences.items():
    time = ottawa_time + value
    
    # Adjust for overflow or underflow in military time
    if time < 0:
        time += 2400
    elif time >= 2400:
        time -= 2400
        
    # Ensure minutes stay within 00-59 range
    hours = time // 100
    minutes = time % 100
    if minutes >= 60:
        # swapping minutes with hours (removing 60 minutes for one hour, same thing)
        # this way we don't have irreigular times like 3 75 
        
        minutes -= 60
        hours += 1
    if hours >= 24:
        hours -= 24
    
    # Format time as military time (HHMM)
    military_time = hours * 100 + minutes
    print("{} in {}".format(military_time, key))
