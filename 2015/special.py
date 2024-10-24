# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# special day
# 25 oct 2024

month = int(input())
day = int(input())

if (month == 2 and day == 18):
    print("Special")

elif (month > 2) or (month == 2 and day > 18):
    print("After")

elif (month < 2) or (month == 2 and day < 18):
    print("Before")
