# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA 
# ccc j3 art 
# 29 nov 2024

number_coors = int(input())

# The top right corner is made up of the maximum x-coordinate found in the set
# of points plus one (as points on the border do not fit) and the maximum
# y-coordinate plus one.
#
# We initialize these variables at -1 as all point's x and y coordinates must be
# > -1. Thus, these variables take on the values of the first point at the
# start without any special-casing needed.
max_x = -1
max_y = -1

# Similar idea for the bottom left corner, except its the minimum x and y
# coordinates.
min_x = 101
min_y = 101

# We use _ because we do not need a counter variable 
# We are simply using the for loop to iterate multiple times so we repeat a block of logic within the loop block

for _ in range(number_coors):
    coor = input().split()

    x = int(coor[0])
    y = int(coor[1])

    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y

print("{},{}".format(min_x - 1, min_y - 1))
print("{},{}".format(max_x + 1, max_y + 1))
