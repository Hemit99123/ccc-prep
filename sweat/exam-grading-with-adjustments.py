# Hemit Patel
# ICS3U0-4
# 781159
# MR VEERA
# exam grading with adjustments
# 24 oct 2024

grade = int(input("Enter your grade:"))
difficult = int(input("Enter the difficulty:"))

# we boost their grade first so that it is reflected
# on their letter grade

if (difficult == 1):
    grade += 5

if (90 <= grade <= 100):
    if (grade == 99):
        print("A+")
    else:
        print("A")

elif (80 <= grade <= 89):
    if (grade == 88):
        print("B+")
    else:
        print("B")
elif (70 <= grade <= 79):
    if (grade == 78):
        print("C+")
    else:
        print("C")
elif (60 <= grade <= 69):
    if (grade == 68):
        print("D+")
    else:
        print("D")
else:
    print("F")


