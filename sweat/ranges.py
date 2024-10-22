# Hemit Patel
# 781158
# ICS3U0-4
# MR VEERA 
# ranges integers
# 21 oct 2024 

user_integer = int(input("Enter an integer:"))

# These ranges are inclusive because the lower-limit of the next range is the next number of the upper-limit of the previous range
# for example in 1-10 range's upper limit is 10 and 11-20 (next range) lower-limit is 11 
# as you can see 11 is the next number after the upperlimit of 10 from the previous range meaning we include 10 in our 1-10 range

if (1 <= user_integer <= 10):
    print("Low")
elif (11 <= user_integer <= 20):
    print("Medium")
elif (21 <= user_integer <= 30):
    print("High")

# otherwise, if the int does not fit into any of these ranges, it means it is not in a recongized range so we output out of range

else:
    print("Out of range")