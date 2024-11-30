# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA 
# ccc j3 art 
# 29 nov 2024

number_coors = int(input())


# The top right and bottom left boundary coordinates have a pattern
# This pattern for bottom left is where the coordinates consist of the smallest x value - 1 and smallest y value -1
# The pattern for top right is where the coordinates consist of the largest x value + 1 and largest y value + 1 

# There is the modification to these values by -1 or +1 because other points within the box will not be fully accounted 
# These modifications acts as buffers for the values ensuring that even if the value was very close to the box, 
# it will be accounted for because we have moved 1 unit forward (+1) or backwards (-1)


# We now initialize the variables max_x, max_y, min_x and min_y to keep track of the smallest/highest x and y values

# We initialize variables: max_x and max_y at -1 as all point's x and y coordinates must be
# > -1 as stated by the boundary. Therefore this value is bound to change within our computation 
# Some coordinates could be 0 and therefore it is not used

max_x = -1
max_y = -1

# Similar idea for the bottom left corner, except its the minimum x and y
# coordinates except values cannot exceed 100, therefore this value is ALSO
# bound to be changed

min_x = 101
min_y = 101

# We use _ because we do not need a counter variable 
# We are simply using the for loop to iterate multiple times so we repeat a block of logic within the loop block
# Here we are repeating the same logic for the amount of coordinates that the user needs 

for _ in range(number_coors):
    # We split the coor so that we can get each of the values (x,y)
    # It creates a list
    
    coor = input().split()

    # Now we use that new list created and get the speific coordinate points 

    x = int(coor[0])
    y = int(coor[1])

    # Here we check if we need to change the values as MAYBE the current x and y values surpass the max/min values

    if x > max_x:
        max_x = x
    if x < min_x:
        min_x = x
    if y > max_y:
        max_y = y
    if y < min_y:
        min_y = y


# Output the final result in the format X,Y using .format() and strings 

print("{},{}".format(min_x - 1, min_y - 1))
print("{},{}".format(max_x + 1, max_y + 1))
