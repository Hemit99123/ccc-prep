# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 22 oct 2024
# problem: ccc 08 j1 - body mass index

# float values because sample inputs were decimals
weight = float(input())
height = float(input())

body_mass_index = (weight) / (height * height)

# checking for the classification.
# the range is inclusive which is why i added = on top of <

if (body_mass_index < 18.5):
    print("Underweight")

elif (18.5 <= body_mass_index <= 25.0):
    print("Normal weight")

# there is no other scenario for classification, so if it isnt underweight or normal weight
# it has to be overweight

else:
    print("Overweight")
