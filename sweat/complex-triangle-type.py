# Hemit Patel
# ICS3U0-4
# 781159
# MR VEERA
# complex triangle type
# 24 oct 2024

a_side = int(input())
b_side = int(input())
c_side = int(input())

is_right_angle = (a_side ** 2 + b_side ** 2) == c_side ** 2

a_b_eq = a_side == b_side
a_c_eq = a_side == c_side
b_c_eq = b_side == c_side

if (a_side == b_side == c_side):
    print("Equilateral")

elif (a_b_eq) or (a_c_eq) or (b_c_eq):
    if (is_right_angle):
        print("Special Right Isosceles")
    else:
        print("Isosceles")

elif not (a_b_eq) or (a_c_eq) or (b_c_eq):
    if (is_right_angle):
        print("Right Scalene")
    else:
        print("Scalene")
