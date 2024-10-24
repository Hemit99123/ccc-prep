# Hemit Patel
# ICS3U0-4
# 781159
# MR VEERA
# quadrant selection
# 24 oct 2024

# the coordiante pair
x = int(input())
y = int(input())

quadrant = 0

if (x > 0 and y > 0):
    quadrant = 1

elif (x < 0 and y > 0):
    quadrant = 2

elif (x < 0 and y < 0):
    quadrant = 3

elif (x > 0 and y < 0):
    quadrant = 4


print("The quadrant is", quadrant)
