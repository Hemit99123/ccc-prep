# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# grading classification (pt III)
# 24 oct 2024

grade = int(input("Enter the grade you earned:"))


if not (0 <= grade <= 100):
    print("Invalid score. Please enter a score between 0 and 100.")
elif (90 <= grade <= 100):
    print("A")
elif (80 <= grade <= 89):
    print("B")
elif (70 <= grade <= 79):
    print("C")
elif (60 <= grade <= 69):
    print("D")
else:
    print("F")
