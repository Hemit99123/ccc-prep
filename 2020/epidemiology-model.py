# Hemit Patel
# 781159
# ICS3U0-1
# J2 2020 Waterloo Solution
# Mr Veera
# 24 sep 2024

people_infected_target = int(input());

people_infected_day0 = int(input());

people_infected_rate = int(input());


days = 1
prev_day_infected = people_infected_day0
total_infected = people_infected_day0

while True:
    people_infected_on_day = prev_day_infected * people_infected_rate
    total_infected += people_infected_on_day
    
    if total_infected > people_infected_target:
        break;
    
    days += 1
    prev_day_infected = people_infected_on_day


print(days)
