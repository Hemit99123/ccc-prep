# Hemit Patel
# STUDENT NUMBER
# ICS3U0-4
# J2 2020 Waterloo Solution
# Mr Veera
# 2 dec 2024


# All the inputs required by the program
people_infected_target = int(input());

people_infected_day0 = int(input());

people_infected_rate = int(input());

# The day counter, it will be incremented everytime the loop is able to run
days = 0

# This is used to keep reference of the how many were infected in the previous day, starts with the ones infected on day 0
prev_day_infected = people_infected_day0

# The total amount infected as the days go on
total_infected = people_infected_day0

while True:

    # Stop the loop if the total infected has surpassed the people infected target as we have found the amount of days already
    if total_infected > people_infected_target:
        break;

    # Calculating how many people were infected on a speific day through a pattern which includes the previous days infected amount * infected rate
    people_infected_on_day = prev_day_infected * people_infected_rate

    # Update the total infected amount by increment the newly infected people
    total_infected += people_infected_on_day

    # Increment one day as a day has just based
    days += 1

    # Changing the prev day to this day as this execution of the loop as now stopped
    prev_day_infected = people_infected_on_day

    


print(days)
