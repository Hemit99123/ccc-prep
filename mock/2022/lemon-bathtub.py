# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Square Root Decompisiton

n = int(input(""))
i = int(input(""))
j = int(input(""))


# Calculate the squared values
i_sq = i ** 2
j_sq = j ** 2

# Calculate the absolute differences from sqrt(n)
# we just want to the difference between the 2 values, not if it resulted in a negative or postive int 
# so the abs value will ensure of that 
# the python function abs() takes input of x and output the absoulte difference from 0 

difference_i = abs(n - i_sq)
difference_j = abs(n - j_sq)

# Compare the differences and print the result
if difference_i < difference_j:
    print("1")  # i's square is closer to the square root of n
else:
    print("2")  # j's square is closer to the square root of n
