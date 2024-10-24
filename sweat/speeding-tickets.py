# Hemit Patel
# ICS3U0-4
# 781159
# MR VEERA
# speeding tickets
# 24 oct 2024

speed_limit = int(input("Enter a speed limit:"))
driver_speed = int(input("Enter the driver's speed:"))
holiday = int(input("Is it a holiday?"))

difference = driver_speed - speed_limit

if (driver_speed <= speed_limit):
    fine = 0
elif (1 <= difference <= 10):
    fine = 50
elif (11 <= difference <= 20):
    fine = 100
elif (21 <= difference <= 30):
    fine = 200
else:
    #  each km/h over 30.
    fine = 200 + (difference-30) * 10

if (holiday == 1 and fine > 0):
    fine = fine * 2

if (fine == 0):
    print("No fine due today")
else:
    print(f"The fine due today is ${fine}")
