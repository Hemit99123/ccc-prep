# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA 
# The Cell Sell 

daytime_mins = int(input())
night_mins = int(input())
weekend_mins = int(input())

# Plan A costs

if (daytime_mins < 100):
    plan_a_daytime = 0
else:
    plan_a_daytime = (daytime_mins - 100) * .25

plan_a_evening = night_mins * .15
plan_a_weekend = weekend_mins * .20

total_a_cost = plan_a_daytime + plan_a_evening + plan_a_weekend

# Plan B costs

if (daytime_mins < 250):
    plan_b_daytime = 0
else:
    plan_b_daytime = (daytime_mins - 250) * .45

plan_b_evening = night_mins * .35
plan_b_weekend = weekend_mins * .25

total_b_cost = plan_b_daytime + plan_b_evening + plan_b_weekend

print(f"Plan A costs {total_a_cost:.2f}")
print(f"Plan B costs {total_b_cost:.2f}")

if (total_a_cost < total_b_cost):
    print("Plan A is cheapest.")

elif (total_b_cost < total_a_cost):
    print("Plan B is cheapest.")

else:
    print("Plan A and B are the same price.")