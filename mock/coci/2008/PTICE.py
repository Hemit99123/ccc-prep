# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# PTICE 

number_questions = int(input("Enter number of questions:"))

# turning into a list so we can iterate over it to check EACH value one by one when checking for correctness
correct_sequence = list(input("Enter the correct answers:"))

# these are the patterns for each of the different persons
adrian = ["A", "B", "C"]
bruno = ["B", "A", "B", "C"]
goran = ["C", "C", "A", "A", "B", "B"]

# the amount of values that must be either deduced or added so that the sequence is the same as the number of questions (number_questions int)
adrian_leftover = number_questions - len(adrian)
bruno_leftover = number_questions - len(bruno)
goran_leftover = number_questions - len(goran)

# Extend or trim `adrian`
if adrian_leftover > 0:
    # if positive int, we add!
    # we will add the different indexes based on the current range
    # so if our range was 2 then we would add index 0 to our list again and then index 1 to our list again so now we have that missing 2 values 
    
    for index in range(adrian_leftover):
        adrian = adrian + [adrian[index]]
else:
    # we simply remove the elements that the number of questions is so that it would equate to the same amount of items as the number itself
    # we do this through slicing which will select a specific amount of values
    adrian = adrian[:number_questions]

# same logic applies to the rest for loops that look similar

# Extend or trim `bruno`
if bruno_leftover > 0:
    for index in range(bruno_leftover):
        bruno = bruno + [bruno[index]]
else:
    bruno = bruno[:number_questions]
# Extend or trim `goran`
if goran_leftover > 0:
    for index in range(goran_leftover):
        goran = goran + [goran[index]]
else:
    goran = goran[:number_questions]

# now we check if answers are correct
adrian_correct_counter = 0
bruno_correct_counter = 0
goran_correct_counter = 0

# run in the range of number questions so we get an index that represents the current position within the list 
for index in range(number_questions):
    # here we simply check if both positions that are in the 2 different lists are correct and equal to one another
    if (adrian[index] == correct_sequence[index]):
        adrian_correct_counter += 1
    if (bruno[index] == correct_sequence[index]):
        bruno_correct_counter += 1
    if (goran[index] == correct_sequence[index]):
        goran_correct_counter += 1

# max gets the maximum values of the different argument values presented 
maximum_value = max(adrian_correct_counter, bruno_correct_counter, goran_correct_counter)

print(maximum_value)

if (adrian_correct_counter == maximum_value):
    print("Adrian")

if (bruno_correct_counter == maximum_value):
    print("Bruno")

if (goran_correct_counter == maximum_value):
    print("Goran")
