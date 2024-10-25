# Hemit Patel
# 781159
# ICS3U0-4
# telephone bill
# MR VEERA
# 25 oct 2024

calls = int(input())

if (calls <= 400):
    rent = 400
else:
    rent = 500


if (calls <= 150):
    call_cost = 0

# 150 calls were used from above statement so we have to account for it here

elif (151 <= calls <= 400):
    call_cost = (calls-150) * 0.8

elif (401 <= calls <= 1000):
    call_cost = 250 * 0.8 + (calls-400) * 1

else:
    call_cost = 250 * 0.8 + 600 + (calls-1000) * 1.20

total_price = rent + call_cost

print("Total bill=", total_price)
