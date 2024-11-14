# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 29 oct 2024 
# fergusonball rating 

players = int(input())

star_players = 0

for _ in range(players):
    points = int(input())
    fouls = int(input())

    scores = (points * 5) - (fouls * 3)
    if (scores > 40):
        star_players += 1

if (star_players == players):
    print(str(star_players) + "+")
else:
    print(str(star_players))
        
