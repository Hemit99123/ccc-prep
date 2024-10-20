# Hemit Patel
# MR VEERA 
# ICS3U0-4
# Oct 20 2024
# CCC '06 - J2 Roll the dice

die_a_sides = int(input())
die_b_sides = int(input())
counter = 0

for die_a in range(1, die_a_sides + 1):
  for die_b in range(1, die_b_sides + 1):
    if (die_a + die_b == 10):
      counter += 1

if (counter == 1):
  print("There is 1 way to get the sum 10.")
else:
  print(f"There are {counter} ways to get the sum 10.")
