# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Triangle Times
# 14 oct 2024

angle_1 = int(input("Enter the first angle:"))
angle_2 = int(input("Enter the second angle:"))
angle_3 = int(input("Enter the thrid angle:"))


# Some variables needed for the conditonal statement 
# This will make it easier for devs to read my program
# Also helps reduce reduncny in my program which means
# It is following the DRY principle

sum_angles = angle_1 + angle_2 + angle_3

# These are the different combinations to see if 2 angles are the same
# There are 6 total but some are un-nesscary as they will produce the same
# operation as one here

one_two_eq = angle_1 == angle_2
one_three_eq = angle_1 == angle_3
two_three_eq = angle_2 == angle_3


if (angle_1 == 60 and angle_2 == 60 and angle_3 == 60):
    print("Equilateral")

# Equlateral is checked first because 60*3 = 180 so it would be true 
# Even if the triangle were Equlateral

# Same logic here, the Iscosceles is checked first because Scalene would 
# be true even if 2 of the angles are the same as the sum would still be 180

elif (sum_angles == 180 and one_two_eq or one_three_eq or two_three_eq):
    print("Isosceles")

elif (sum_angles == 180):
    print("Scalene")

# If none of these combinations work, it is an error so print that out

else:
    print("Error")
