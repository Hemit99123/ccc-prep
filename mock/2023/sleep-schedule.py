# Hemit Patel
# 781159
# MR VEERA
# ICS3U0-4
# 22 oct 2024
# sleep schedule 

bedtime_hour = int(input())
waketime_hour = int(input())

if (waketime_hour < bedtime_hour):
    # if waketime is less than bedtime hour, it means we are in the next day
    # so to reflect we are in the next day, we must add 24 to the waketime hour so that we know a day has gone by
    
    difference = (waketime_hour + 24) - bedtime_hour

# Now we check for 3 different conditions. each of these conditions must be true to output healthy hence the boolean operaters of and

if (20 <= bedtime_hour <= 23) and (6 <= waketime_hour <= 9) and (8 <= difference <= 10):
    print("Healthy")
else:
    print("Unhealthy")
