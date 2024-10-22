# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 22 oct 2024
# problem: try angles

num_triangles = int(input())

for _ in range(num_triangles):
    angles = input()
    angles_list = angles.split()
    if (int(angles_list[0]) + int(angles_list[1]) + int(angles_list[2]) == 180):
        print("valid")
    else:
        print("invalid")
