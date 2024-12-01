# Hemit Patel
# STUDENT NUMBER
# ICS3U0-4
# J2 2020 Waterloo Solution
# Mr Veera
# 2 dec 2024


# Input
target_infections = int(input())  # Target total number of people infected
initial_infections = int(input())  # People infected on Day 0
infection_rate = int(input())  # Number of people each infected person infects

# Initialize variables
total_infected = initial_infections  # Total number of people infected so far
current_day_infections = initial_infections  # Infections on the current day
day = 0  # Start counting from Day 0

# We use a while loop because we have a condition for when the loop ends, meaning we do not know EXACTLY 
# how many iterations there will be, just when it will break
# We need to repeatly keep calculating the computation because each day requires computation 
# which means we have to repeat for EACH AND EVERY DAY


# The loop will only continue if the total infected has NOT surpassed the people infected target as 
# if that were the case, we have found the amount of days already (the end condition)

while total_infected <= target_infections:

    # Increment one day as a day has just passed by with each iteration

    day += 1  # Move to the next day

    # Calculating how many people were infected on a speific day through a pattern which includes the previous days infected amount * infected rate

    current_day_infections *= infection_rate  

    # Update total infections with the current day infection to keep it for record 
    # We need this number to be updated as it is used as a counter for 
    # our while loop to ensure the loop stops at the correct time

    total_infected += current_day_infections 

# Output the first day when the total exceeds the target 
# (as the while loop will stop executing by then)

print(day)