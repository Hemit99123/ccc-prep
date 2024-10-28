# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# shifty sum
# 28 oct 2024 

number = int(input())
amount_shifted = int(input())

# this is to keep track of the different numbers

# this is our total sum 
sum = number

# this is the previous number that was added to the sum
prev_num_added = number

# in this loop we will "shift" the number by the amount of times the user inputted
# the shifting would multiply the initial digit 10 times each execution of this repeated loop

for number in range(amount_shifted):
  # we shift the digit by 10 by multiplying 10 here
  current_num = prev_num_added * 10
  # add to the sum by incrementing it using the +=
  sum += current_num
  # set the now previous number added to the sum to the current number
  prev_num_added = current_num

# print out the sum
print(sum)
