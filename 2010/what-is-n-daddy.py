# Hemit Patel
# MR VEERA 
# ICS3U0-4 
# Oct 19 2024
# CCC '10 J1 - What is n, Daddy?

## REGULAR SOLUTION 
import sys 

# This is just like the input() function but much more faster 
number = sys.stdin.readline("Enter the amount Natalie has to show:")
number = int(input("")
             
total_ways = 0

# Checking if number on one hand is possible

if (number <= 5):
  total_ways += 1

# Now we go check for the different combinations of the two hands (hand a will always be larger then hand b)
# This is why we don't check for equations like 1+3 or 2+4 because the hand a is smaller than hand b
# They are not elif statements because we want to check for all the possible combinations, each condition does not rely on the result of the previous condition 

if (5+1 == number):
  total_ways += 1

if (5+2 == number):
  total_ways += 1

if (5+3 == number):
  total_ways += 1

if (5+4 == number):
  total_ways += 1

if (5+5 == number):
  total_ways += 1

if (4+1 == number):
  total_ways += 1

if (4+2 == number):
  total_ways += 1

if (4+3 == number):
  total_ways += 1

if (4+4 == number):
  total_ways += 1

if (3+1 == number):
  total_ways += 1

if (3+2 == number):
  total_ways += 1

if (3+3 == number):
  total_ways += 1

if (2+1 == number):
  total_ways += 1

if (2+2 == number):
  total_ways += 1

if (1+1 == number):
  total_ways += 1

print(total_ways)

# ADVANCED BETTER SOLUTION (LEARN BETTER TMR USES LOOPS -> GOTTA EXPLAIN THAT TOO IF U WANNA USE IT ON THE TEST)

number = int(input("Enter the amount Natalie has to show:"))
total_ways = 0
hand = [number,0]

while True:
    if hand[0] <= 5 and hand[1] <= 5:
        total_ways += 1
    hand[0] -= 1
    hand[1] += 1
    if hand[0] < hand[1]:
        break
print(total_ways)
