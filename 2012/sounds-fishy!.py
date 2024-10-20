# Hemit Patel
# MR VEERA 
# ICS3U0-4
# Oct 20 2024
# CCC '12 J2 - Sounds Fishy!

# All integers are on their own input line so we assign different variables for each of them
# in the sequence

depth_1 = int(input())
depth_2 = int(input())
depth_3 = int(input())
depth_4 = int(input())

# Check if all depths are the same. We check for the larger one to the smaller one for comparsion. If we did it the other way around, the comparsion would be flipped
# meaning fish rising would have to be checked with < and fish diving would have to be checked with >

if (depth_2 == depth_1 and depth_3 == depth_2 and depth_4 == depth_3):
  print("Fish At Constant Depth")

elif (depth_2 > depth_1 and depth_3 > depth_2 and depth_4 > depth_3):
  print("Fish Rising")

elif (depth_2 < depth_1 and depth_3 < depth_2 and depth_4 < depth_3):
  print("Fish Diving")

else:
  print("No Fish")
