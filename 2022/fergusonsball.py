# Hemit Patel
# STUDENT NUMBER
# ICS3U0-1 (Course code)
# J2 2022 Solution
# INSTRUCTOR NAME
# 21 sep 2024

number_players = int(input(""));
amount = 0;

# Run the same program each time for each player so that we can see each players rating

for _ in range(number_players):

    # This is the 2 inputs which will collect the player data
    points = int(input(""));
    fouls = int(input(""));

    # The processing based on the constraints given to see if a rating is above 40 stars
    star_rating = (points * 5) - (fouls * 3);

    # If it is, increment one to the amount variable which will serve as an output
    if star_rating > 40:
        amount += 1;
'''
Here we are checking if a team is a "gold" team by seeing if the amount of players
above 40 ratings is the same as the ACTUAL amount of players on said team
'''

if amount == number_players:
    print(str(A) + "+");
else:
    print(str(A));
    
