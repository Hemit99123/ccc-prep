# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# leap year
# 23 oct 2024

year = int(input("Enter a year: "))

'''
Example Problem 2: "Leap Year"
Problem:
A year is a leap year if:

It is divisible by 4, and
If it is divisible by 100, it must also be divisible by 400. Write a program that determines if a given year is a leap year.
Input:

One integer representing the year.
Output:

Print "Leap year" if it is a leap year, or "Not a leap year" otherwise.
'''
# here we are checking if year is divisable by 4
# and we also want to ensure that year IS NOT by 100
# we also check if it is then it should be divisable by 400
# we use or because only one of the statements can be true
# if the year is divisable by 100 it should be divisbale by 400 hence the first
# comparision of it NOT being divisbale of 100 would be false
# the opposite holds true for when year % 100 == 0


if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
    print("Leap year")


# if this logic does not hold true, it is not a leap year
else:
    print("Not a leap year")
