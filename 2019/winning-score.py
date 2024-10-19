# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Winning Score J1 2019

# Inputs grouped based on the team (for better readablity)

apple_three_points = int(input())
apple_two_points = int(input())
apple_one_points = int(input())

bananas_three_points = int(input())
bananas_two_points = int(input())
bananas_one_points = int(input())

# The scores are calculated with multiplication because the inputs are just the AMOUNT of scores of each type
total_apple_score = (apple_three_points * 3) + (apple_two_points * 2) + (apple_one_points * 1)

total_bananas_score = (bananas_three_points * 3) + (bananas_two_points * 2) + (bananas_one_points * 1)

# Checking for eqaulity which means tie
if (total_apple_score == total_bananas_score):
    print("T")
# Otherwise if apple is grater than bananas
elif (total_apple_score > total_bananas_score):
    print("A")
# Otherwise if bananas is grater than apples
else:
    print("B")
