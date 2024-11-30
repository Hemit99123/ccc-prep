# Hemit Patel
# STUDENT NAME
# ICS3U0-1 (Course code)
# J2 2021 Solution
# INSTRUCTOR NAME
# 22 sep 2024

amount_bidders = int(input())

# max is used to track the highest bid 
max_bid = 0

# this is used to track the winner of the bid
winner = ""


# We do not need a counter variable hence the _ (it is there as a placeholder)
# We are simply using the for loop to repeat logic 

for _ in range(amount_bidders):
    # we get the name and bid for this spefic bid
    name = input()
    bid = int(input())

    # if the current bid given is higher than the max bid
    # That means the current bid is now the max big 
    # And therefore the current bidder is named winner
    if bid > max_bid:
        max_bid = bid
        winner = name


# Whoever is able to stay winner after the loop is printed 
# Becuase the winner might change as the loop iterates 
# and gets more bids from other bidders

print(winner)
