# Hemit Patel
# STUDENT NAME
# ICS3U0-1 (Course code)
# J2 2021 Solution
# INSTRUCTOR NAME
# 22 sep 2024

N = int(input(""));
bid = 0
winner = 0

for _ in range(N):
    name = input("");
    amount = int(input(""));

    if amount > bid:
        bid = amount
        winner = name


print(winner)
    

    
