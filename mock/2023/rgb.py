# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 30 nov 2024
#  ccc j3 rgb

length_str = input()
word = input()

rgb_count = 0
g_count = 0


for letter in word:
    if (letter == "R"):
        g_count = 0
    elif (letter == "B" and g_count == 1):
        rgb_count += 1
    elif (letter == "G"):
        g_count += 1

print(rgb_count)