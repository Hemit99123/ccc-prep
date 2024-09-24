# Hemit Patel
# STUDENT NUMBER
# ICS3U0-1
# J1 2020 Solution
# INSTRUCTOR NAME
# 23 sep 2024

# The input variables that will be fed into the program

small_treat = int(input(""));
medium_treat = int(input(""));
large_treat = int(input(""));

# The output is a formula that is given in the question
# This formula when computed will provide a score that can be used to determine if dog is happy/sad

happiness_score = 1 * small_treat + 2 * medium_treat + 3 * large_treat

# Now using the score we can determine if the dog is happy (above 10 score) or sad

if happiness_score >= 10:
    print("happy")
else:
    print("sad")
