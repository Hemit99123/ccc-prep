# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Special Day

month = int(input())
day = int(input())

# PUT ALL CONDITIONS FOR ONE OUTPUT IN ONE IF STATEMENT (FOR TEST)
# LINK THEM WITH THE BOOLEAN OPERATORS OF AND AND OR

if (month == 2 and day == 18):
    print("Special")

elif (month == 2 and day < 18) or (month < 2):
    print("Before")

elif (month == 2 and day > 18) or (month > 2):
    print("After")
