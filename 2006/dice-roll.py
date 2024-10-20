# Hemit Patel
# MR VEERA 
# ICS3U0-4
# Oct 20 2024
# CCC '06 - J2 Roll the dice

die_a_sides = int(input())
die_b_sides = int(input())
counter = 0

# Going through the range of die_a which is 1 to die_a_sides (inclusive)
# This is why we add one to the upper limit because in the range() upper limit is not used 
# It will iterate for each number in that range so linear time O(n)

for die_a in range(1, die_a_sides + 1):
  # For each number in the range a, we want to check it with the range of die_b so we run a nested range
  for die_b in range(1, die_b_sides + 1):
    # Checking if both numbers added == 10 
    if (die_a + die_b == 10):
      # If so, increment the count because it is a way you can add 10 with the numbers on the die
      counter += 1

# Checking if counter is 1 as it outputs diferently
# Instead of ways, we say way 
# Instead of are, we say is 

if (counter == 1):
  print("There is 1 way to get the sum 10.")

# Otherwise the default way is fine, we need the variable counter in the string itself
# Because the value is unknown unlike the if statement where we know the counter == 1
else:
  print(f"There are {counter} ways to get the sum 10.")
