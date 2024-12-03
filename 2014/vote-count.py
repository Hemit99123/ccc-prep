# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA 
# VOTE COUNT q1
# 2 dec 2024

vote_seq = input("Enter the votes:")

a_count = 0
b_count = 0

# The vote seq contains the votes for either A or B
# Go through each character to figure out if it is A or B
# And increment the respective counter

# We use a for loop because we have a list meaning an iterable data strcuture
# Each vote will be ONE singular character from the variable vote_seq

for (vote in vote_seq):

    # Vote contains a character from vote_seq

    # Here we check if vote is A or B
    # Whichever it is we increment the respective counter
    # using the += which assigns to the variable itself + an integer
    # e.g. a_count += 1 would just be a_count = a_count + 1
    # This way we keep the count of the current votes but add another new vote
    
    if (vote == "A"):
        a_count += 1

    # There can only be two types of votes, A or B
    # Therefore we can simply use an else statement because
    # There is no other scenario
    
    else:
        b_count +=1


# Now see the results based on the vote count done for the for loop
# If both a_count and b_count is the same, then it is a tie

if (a_count == b_count):
    print("It is a Tie")

# If it isn't a tie, a vote (A/B) has won!
# Therefore we must find that vote through using the comparsion operators: < or >

# Here we check if a_count is greater than b_count
# In which case a wins, but since it is an ELIF it will only run if
# the vote wasn't a tie

elif (a_count > b_count):
    print("A is the winner")

# There is only one other scenario where B is the winner
# Because you are comparing ONLY 2 variables and seeing which vote is greater
# Therefore we can simply use an else statement for the ONLY next outcome!

else:
    print("B is the winner")
