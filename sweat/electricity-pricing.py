# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 23 oct 2024
# electricity bill calculator

kwh_used = int(input())
cost = 50

cost += 100 * 0.3

if (kwh_used <= 100):
    cost += 100 * 0.3
elif (101 <= kwh_used <= 300):
    cost += (100*0.3) + (kwh_used - 100) * 0.5
else:
    cost += (100*0.3) + (200*0.5) + (kwh_used - 300) * 0.75

if (kwh_used > 500):
    cost += 100

if (kwh_used < 50):
    cost -= cost * 0.1
