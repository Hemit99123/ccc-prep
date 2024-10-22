# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA 
# weather 
# 21 oct 2024

weather = int(input("Enter the temperature in Celsius"))
category = ""

# it was worded 0 AND below meaning that 0 is also included in this category
if (weather <= 0):
    category = "Freezing"

# since 0 is included in the other category, we cannot include it in this range
# 15 is included because it says up "to"
# this same logic applies for all other ranges

elif (0 < weather <= 15):
    category = "Cold"
elif (15 < weather <= 25):
    category = "Mild"
elif (25 < weather <= 35):
    category = "Warm"

# if it isn't any of these ranges, it must be above 35 because the last range checks from 26 to 35 
# for that we have hot 
# we use else statement because there is no other condition to check so it helps keep the logic clean

else:
    category = "Hot"

print(f"You are in the {category} category.")