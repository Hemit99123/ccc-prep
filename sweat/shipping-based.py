# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# shipping based pricing
# 24 oct 2024

weight = int(input("Enter the amount of weight:"))

cost = 10

if (5 < weight <= 20):
    cost += (weight - 5) * 5

elif (weight > 20):
    cost += (weight - 20) * 10
