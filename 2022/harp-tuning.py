# Hemit Patel
# STUDENT NUMBER
# ICS3UO-1
# Harp Tuning Convertor
# INSTRUCTOR NAME
# 25 nov 2024

tuning_instruction = input("")

# Convert the tuning instruction into a list of characters
tuning_instruction = list(tuning_instruction)

current_instruction = ""

# Loop through each character in the tuning instruction
for idx in range(len(tuning_instruction)):
    if tuning_instruction[idx] == "+":
        current_instruction += " tighten "
    elif tuning_instruction[idx] == "-":
        current_instruction += " loosen "
    elif tuning_instruction[idx] in "0123456789":
       current_instruction += tuning_instruction[i]
       if i + 1 == len(tuning_instruction) or tuning_instruction[idx+1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            print(current_instruction)
            current_instruction = ""
    else:
        current_instruction += tuning_instruction[i]
