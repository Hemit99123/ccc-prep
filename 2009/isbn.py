# Hemit Patel
# 781159
# MR VEERA 
# ICS3U0-4
# CCC 09 J1 - ISBN
# 20 oct 2024

first_ten_digits = 9780921418

# The last 3 digits for the isbn code
last_digit_1 = int(input())
last_digit_2 = int(input())
last_digit_3 = int(input())

# Concat the last digits to the first_ten_digits
# We can only concat strings so we convert them into strings but then convert it back into an integer after the operation
final_digits = int(str(first_ten_digits) + str(last_digit_1) + str(last_digit_2) + str(last_digit_3))

# This tag will change from 1 or 3 so we can see what number to multiply by 
# It acts as a pointer/reference for us
tag = 1 

total = 0


# int cannot be iterable so we must change them back to a string which is iterable
# we go through each digit one by one through for loop so we can multiply each digit by tag

for digit in str(final_digits):
    # Check which tag we are using and use that for multiplication

    if (tag == 1):
        total += (int(digit) * 1)
        # changing tag to 3 so we are alternating as it is currently 1
        tag = 3

    # It can only be either 1 or 3 because we only set it to those values, so no need for elif 
    # else would work because there is no other circumstance
    
    else:
        total += (int(digit) * 3)
        # changing tag to 1 because it is currently 3 
        tag = 1

print("The 1-3-sum is", total)

## BONUS -> 

# check if isbn number is valid 
# the 1-3 sum must be a multiple of 10 for it to be a valid number

# % 10 checks for the remainders when total is int divided by 10 
# if there are none that means all numbers were sucessfully grouped so it is a multiple of 10!

if (total % 10 == 0):
    print("valid isbn number")
else:
    print("invalid ibsn number")