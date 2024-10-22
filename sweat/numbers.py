# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 22 oct 2024
# problem: numbers

'''
Create a program that takes a digit of 0-9. Then convert the digit into word form. If not in range, output an error
'''

number = int(input("Enter a number:"))

# we first check if it is NOT in the range of 0 to 9
# we can use the NOT keyword which checks for the False value in a comparsion operator
# if false than it produces a true for the if statement

if (not 0 <= number <= 9):
    print("Not in the range")

# if this produced a false, that means that the comparsion operator was true so we are in the range
# so we can continue our logic of checking what the number is and outputting the alphanumeric numeral

elif (number == 0):
    print("zero")
elif (number == 1):
    print("one")
elif (number == 2):
    print("two")
elif (number == 3):
    print("three")
elif (number == 4):
    print("four")
elif (number == 5):
    print("five")
elif (number == 6):
    print("six")
elif (number == 7):
    print("seven")
elif (number == 8):
    print("eight")
elif (number == 9):
    print("nine")
