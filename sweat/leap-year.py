# Hemit Patel
# 781159
# MR VEERA
# ICS3U0-4
# leap year checker
# 24 oct 2024

'''

Problem 5: Leap Year Checker
Write a program that checks whether a given year is a leap year. A year is a leap year if:

It is divisible by 4, but not divisible by 100, unless it is also divisible by 400.
Input:

A single integer representing the year.
Output:

"Leap Year" if the year is a leap year, otherwise "Not a Leap Year."

'''
year = int(input("Enter the year:"))

# the first condition checks for when year is not divisable by 100
# so we only need to check if year is divisable by 4

# the next condition checks for when year IS divisable by 100 (century) in which
# it needs to be disiable by 4 and 400

# only one of these conditions can be true at a time because if a number
# makes the first condition true that means year is not divisable by 100
# so the second condition would become false

if (year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
