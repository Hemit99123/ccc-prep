# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# occupy parking question
# 28 oct 2024 

number_parking = int(input())

# turn the inputs into a list of characters 
# this way we can check for each one by one in a for loop

yesterday_parking = list(input())
today_parking = list(input())


# the amount of spaces that will be occupied today AND yesterday
occupied_spaces = 0


# we run the for loop for the amount of parking spaces which is given to us
# as our first int

for parking_index in range(number_parking):
  # here we check the index for both lists and see if they are occupied. 
  # if so we know that both lists have the same index and we can add 1 to the occupied spaces

  # we subtract parking idx by 1 because the index starts at 0 and we want to check the index of the list, so to account for that 0 initial position we take away one
  if (yesterday_parking[parking_index - 1] == "C" and today_parking[parking_index - 1] == "C"):
    occupied_spaces += 1

print(occupied_spaces)
