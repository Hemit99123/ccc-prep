# Hemit Patel
# 781159  
# ICS3U0-4
# Quadrant
# MR VEERA 
# 13 oct 2024

x_coor = int(input("Enter the x coordinate:"))
y_coor = int(input("Enter the y coordinate:"))


# ELIFS are going in the order of the quadrants for better readablity 
# Order in this case does not matter as the conditions do not depened on each other

# Using < and > to determine if integer is negative or positive. If postive it must be above 0 
# if negative it must be below 0

postive_x = x_coor > 0
negative_x = x_coor < 0

postive_y = y_coor > 0
negative_y = y_coor < 0


# Using these variables which determine if numbers are postive or negative with boolean values
# To determine which quadrant the point is in

if (postive_x and postive_y):
  print("1")

elif (negative_x and postive_y):
  print("2")
  
elif (negative_x and negative_y):
  print("3")

elif (postive_x and negative_y):
  print("4")
