# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# PTICE 

number_questions = int(input("Enter number of questions:"))
correct_sequence = list(input("Enter the correct answers:"))

adrian = ["A", "B", "C"]
bruno = ["B", "A", "B", "C"]
goran = ["C", "C", "A", "A", "B", "B"]

adrian_leftover = number_questions - len(adrian)
bruno_leftover = number_questions - len(bruno)
goran_leftover = number_questions - len(goran)

# Extend or trim `adrian`
if adrian_leftover > 0:
    for index in range(adrian_leftover):
        adrian = adrian + [adrian[index]]
else:
    adrian = adrian[:number_questions]

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

adrian_correct_counter = 0
bruno_correct_counter = 0
goran_correct_counter = 0

for index in range(number_questions):
    if (adrian[index] == correct_sequence[index]):
        adrian_correct_counter += 1
    if (bruno[index] == correct_sequence[index]):
        bruno_correct_counter += 1
    if (goran[index] == correct_sequence[index]):
        goran_correct_counter += 1

maximum_value = max(adrian_correct_counter, bruno_correct_counter, goran_correct_counter)

print(maximum_value)

if (adrian_correct_counter == maximum_value):
    print("Adrian")

if (bruno_correct_counter == maximum_value):
    print("Bruno")

if (goran_correct_counter == maximum_value):
    print("Goran")