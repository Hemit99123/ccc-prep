# Hemit Patel
# 781159
# MR VEERA
# ICS3U0-4
# triangle checker
# 24 oct 2024

'''
Problem: Triangle Type Checker
Given the lengths of three sides of a triangle, determine whether the triangle is:

Equilateral (all sides are equal),
Isosceles (exactly two sides are equal),
Scalene (no sides are equal), or
Not a Triangle (the lengths provided cannot form a triangle).
The conditions for a valid triangle are:

The sum of any two sides must be greater than the third side.
Input:

Three integers, representing the lengths of the sides of the triangle.
Output:

One of the following messages: Equilateral, Isosceles, Scalene, or Not a Triangle.


'''
side_length_1 = int(input("Enter side length 1:"))
side_length_2 = int(input("Enter side length 2:"))
side_length_3 = int(input("Enter side length 3:"))

# all the different sums of any 2 sides
sum_s1_s2 = side_length_1 + side_length_2
sum_s1_s3 = side_length_1 + side_length_3
sum_s2_s3 = side_length_2 + side_length_3

if not ((sum_s1_s2 > side_length_3) and (sum_s1_s3 > side_length_2) and (sum_s2_s3 > side_length_1)):
    print("Not a Triangle")

elif (side_length_1 == side_length_2 == side_length_3):
    print("Equailateral")

elif (side_length_1 == side_length_2) or (side_length_2 == side_length_3) or (side_length_1 == side_length_3):
    print("Isosceles")

else:
    print("Scalene")
    
