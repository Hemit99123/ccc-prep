# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# shifty total
# 28 oct 2024 

number = int(input())
amount_shifted = int(input())

# this is to keep track of the different numbers

# this is our total sum 
total = number

# this is the previous number that was added to the total
prev_num_added = number

# in this loop we will "shift" the number by the amount of times the user inputted
# the shifting would multiply the initial digit 10 times each execution of this repeated loop

for number in range(amount_shifted):
  # we shift the digit by 10 by multiplying 10 here
  current_num = prev_num_added * 10
  # add to the total by incrementing it using the +=
  total += current_num
  # set the now previous number added to the total to the current number
  prev_num_added = current_num

# print out the total
print(total)
