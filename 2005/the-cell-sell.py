# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA 
# The Cell Sell 

daytime_mins = int(input())
night_mins = int(input())
weekend_mins = int(input())

# The different minute costs for Plan A 
# All cents are in decimal values because the costs are calculated in dollars and cents is a subunit of it

# Here we are checking if the daytime minutes is under the free allocated time which is 100 minutes 
# If so, the daytime minutes are free
# Otherwise, remove 100 minutes from the daytime minutes and compute so you are still accounting for the free 100 minutes you get

if (daytime_mins < 100):
    plan_a_daytime = 0
else:
    plan_a_daytime = (daytime_mins - 100) * .25


plan_a_evening = night_mins * .15
plan_a_weekend = weekend_mins * .20

# Adding all of the minute costs up for a grand total
total_a_cost = plan_a_daytime + plan_a_evening + plan_a_weekend

# Plan B costs

# same logic for the free minutes as plan a

if (daytime_mins < 250):
    plan_b_daytime = 0
else:
    plan_b_daytime = (daytime_mins - 250) * .45

plan_b_evening = night_mins * .35
plan_b_weekend = weekend_mins * .25

total_b_cost = plan_b_daytime + plan_b_evening + plan_b_weekend

# f string is like .format() function but lets you embed variables using {} instead of in a paramater
# rounding functions are ran with :.NUMBERf 
# we round because inputs are all in 2 decimal places

print(f"Plan A costs {total_a_cost:.2f}")
print(f"Plan B costs {total_b_cost:.2f}")


# Here we check which plan is the (best) a.k.a cheaper hence why we use < symbol

if (total_a_cost < total_b_cost):
    print("Plan A is cheapest.")

elif (total_b_cost < total_a_cost):
    print("Plan B is cheapest.")

# If none of the plans are cheaper than one another, it means the plan cost is equal so use else 
# because there is no other scenario that could play out

else:
    print("Plan A and B are the same price.")