# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Morning Routine
# 21 oct 2024

hours = int(input())
minutes = int(input())

# ADDING ALL THE MINUTES UP WITH THE MINUTES NEEDED TO GET READY FOR THE
# DAY, THAT IS WHY WE ADD 5,10,5,30

total_minutes = (hours * 60) + minutes + 5 + 10 + 5 + 30

# SINCE EVERYTHING IS IN MINUTES, THE BUS ARRIVING IN HOURS MUST BE IN MINUTES TOO
bus_arrives_minutes = 8 * 60

# NOW CHECK IF THE TOTAL MINUTES IS LESS THAN THE BUS ARRIVES
# IF IT IS GREATER THAN WE KNOW KURBYDOO MISSED THE BUS AS THE BUS ALREADY ARRIVED
if (total_minutes <= bus_arrives_minutes):
    print("KURBYDOO MAKES THE BUS")

elif (total_minutes - 30 <= bus_arrives_minutes):
    print("KURBYDOO SKIPS BREAKFAST")

else:
    print("KURBYDOO MISSES THE BUS")
    
