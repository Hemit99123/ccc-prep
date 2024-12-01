# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 1 dec 2024 
# fergusonball rating 

players = int(input())

# Counter for how many star players there are
star_players = 0

# We simply need code to repeat for the amount of players there are, so it runs for each player
# There is no need for a counter variable hence we use the placeholder reserved by python 3 programming language, _

for _ in range(players):
    points = int(input())
    fouls = int(input())

    # Here we calculate the score where points are given 5 ratings each
    # But we take away 3 ratings for each foul hence the subtraction

    scores = (points * 5) - (fouls * 3)

    # If the score is above 40, this player is a STAR so we can increment our counter for that
    if (scores > 40):
        star_players += 1

# If all players are star players which is what we are checking in if statement
# This means that the team is gold and therefore must have a + after the amount of players
if (star_players == players):
    # Doesnt matter if we use star_players or players here because both equal the SAME number
    # Good practice to use star_players though because that is what the output is representing
    print("{}+".format(star_players))
else:
    print("{}".format(star_players))
