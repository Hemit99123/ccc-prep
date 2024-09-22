# Hemit Patel
# STUDENT NUMBER
# ICS3U0-1 (Course code)
# J2 2022 Solution
# INSTRUCTOR NAME
# 21 sep 2024

N = int(input(""));
A = 0;

# Run the same program each time for each player so that we can see each players rating

for _ in range(N):

    # This is the 2 inputs which will collect the player data
    P = int(input(""));
    F = int(input(""));

    # The processing based on the constraints given to see if a rating is above 40 stars
    S = 0;

    S = (P * 5) - (F * 3);

    # If it is, increment one to the amount variable which will serve as an output
    if S > 40:
        A += 1;
'''
Here we are checking if a team is a "gold" team by seeing if the amount of players
above 40 ratings is the same as the ACTUAL amount of players on said team
'''

if A == N:
    print(str(A) + "+");
else:
    print(str(A));
    
