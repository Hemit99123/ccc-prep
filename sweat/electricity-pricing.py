# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 23 oct 2024
# electricity bill calculator

'''

Base Charge:

Every customer is charged a base service fee of $50 per month.
Electricity Usage (in kWh):

For the first 100 kWh of electricity, the cost is $0.30 per kWh.
For the next 200 kWh (i.e., between 101 and 300 kWh), the cost is $0.50 per kWh.
For anything beyond 300 kWh, the cost is $0.75 per kWh.
Peak Usage Charge:

If the usage exceeds 500 kWh, an additional "peak usage" charge of $100 is applied.
Discount for Low Users:

If the total usage is under 50 kWh, the customer gets a 10% discount on their total bill.

'''
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
