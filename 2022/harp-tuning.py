# Hemit Patel
# STUDENT NUMBER
# ICS3UO-1
# Harp Tuning Convertor
# INSTRUCTOR NAME
# 27 nov 2024

tuning_instruction = input("")

current_instruction = ""

# Loop through each character in the tuning instruction
# We use range, so we get a numerical value that represents the current
# position of the string 

for idx in range(len(tuning_instruction)):
    character = tuning_instruction[idx]
    next_character = tuning_instruction[idx+1]
    
    if character == "+":
        current_instruction += " tighten "
    elif character == "-":
        current_instruction += " loosen "
    else:
        current_instruction += character

    if (character in "0123456789" and next_character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ") or (idx + 1 == len(tuning_instruction)):
        print(current_instruction)
        current_instruction = ""
