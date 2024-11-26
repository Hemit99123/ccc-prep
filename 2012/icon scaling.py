# Hemit Patel
# 781159
# MR VEERA
# ICS3U0-4
# 26 nov 2024
# ccc 08 j3

scale = int(input("Enter the scale:"))

# the amount of rows is dependant on k (the scale)

for _ in range(scale):
    print("*" * scale + "x" * scale + "*" * scale)

for _ in range(scale):
    print(" " * scale + "xx" * scale)

for _ in range(scale):
    print("*" * scale + " " * scale + "*" * scale)
