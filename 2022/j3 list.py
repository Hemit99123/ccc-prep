# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# j3 2022 lists solution
# mr. veera
# 20 dec 2024

instruction_line = input()

# Initialize variables

# This includes all the different instructions translated
tuning_list = []

# This is for the current set of letters in the iteration
current_letters = []

# Counter for the while loop
iteration = 0

# Process the input character by character
while iteration < len(instruction_line):
    if instruction_line[iteration] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        # Collect letters
        current_letters.append(instruction_line[iteration])
        iteration += 1
    elif instruction_line[iteration] in '+-':
        # Found a sign, collect the number that follows
        sign = instruction_line[iteration]
        iteration += 1
        number = ""
        while iteration < len(instruction_line) and instruction_line[iteration] in "1234567890":
            number += instruction_line[iteration]
            iteration += 1
            
        # Create instruction tuple and add to list
        action = "tighten" if sign == '+' else "loosen"
        tuning_list.append((''.join(current_letters), action, number))
        
        # Reset letters collection for next instruction
        current_letters = []

# Print output which includes the list of the different instructions
for letters, action, number in tuning_list:
    print(f"{letters} {action} {number}")
