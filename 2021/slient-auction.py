# Hemit Patel
# STUDENT NAME
# ICS3U0-1 (Course code)
# J2 2021 Solution
# INSTRUCTOR NAME
# 22 sep 2024

amount_bidders = int(input())
max = 0
winner = ""

for _ in range(amount_bidders):
    name = input()
    bid = int(input())
    if bid > max:
        max = bid
        winner = name

print(winner)
