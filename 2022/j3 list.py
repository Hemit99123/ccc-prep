# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# j3 2022 - list solution
# 20 dec 2024

tuning_instruction = input()

# This includes all the different instructions translated
# They all are put into a list which will be outputted through a for loop
# at the end of execution

tuning_list = []

# This is for the current set of letters until new instruction
# needs to be translated

current_letters = []

# Counter for the while loop
iteration = 0

# Process the input character by character
while iteration < len(tuning_instruction):
    if tuning_instruction[iteration] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        # Collect letters
        current_letters.append(tuning_instruction[iteration])
        iteration += 1
    elif tuning_instruction[iteration] in '+-':
        # Found a sign, collect the number that follows
        sign = tuning_instruction[iteration]
        iteration += 1
        number = ""
        while iteration < len(tuning_instruction ) and tuning_instruction [iteration] in "1234567890":
            number += tuning_instruction[iteration]
            iteration += 1
            
        # Create instruction string and add to list
        # Did it in a one-liner to save codespace (line of codes)
        
        action = "tighten" if sign == '+' else "loosen"
        
        # Join the letters and create the full instruction
        # It should be a string, hence why we are formatting it with f string
        instruction = f"{''.join(current_letters)} {action} {number}"
        tuning_list.append(instruction)
        
        # Reset letters collection for next instruction through
        # resetting it to a empty list
        
        current_letters = []  

# Print output through iterating over the tuning_list
# Each element which is stored in "instruction" will be a translated instruction
# For the user to see

for instruction in tuning_list:
    print(instruction)
