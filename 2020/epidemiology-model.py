# Hemit Patel
# STUDENT NUMBER
# ICS3U0-1
# J2 2020 Waterloo Solution
# INSTRUCTOR NAME
# 24 sep 2024

people_infected_target = int(input());

people_infected_day0 = int(input());

people_infected_rate = int(input());


days = 0
prev_day_infected = people_infected_day0
total_infected = people_infected_day0

while True:

    if total_infected > people_infected_target:
        break;
    
    people_infected_on_day = prev_day_infected * people_infected_rate
    
    total_infected += people_infected_on_day
        
    days += 1
    prev_day_infected = people_infected_on_day

    


print(days)
