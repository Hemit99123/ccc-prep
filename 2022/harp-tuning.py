# ATTEMPT (DID NOT WORK, DID NOT PROPERLY IMPLEMENT TOKENIZATION AND OTHER LOGIC IS FLAWED)

tuning_instruction = input("Enter the tuning:")

# Convert the tuning instruction into a list of characters
tuning_instruction = list(tuning_instruction)

current_instruction = ""

# Loop through each character in the tuning instruction
for i in range(len(tuning_instruction)):
    if tuning_instruction[i].isalpha():  # Check if the character is a letter
        current_instruction += tuning_instruction[i]
    elif tuning_instruction[i] == "+":  # Check if the character is "+"
        current_instruction += " tightened"
    elif tuning_instruction[i] == "-":  # Check if the character is "-"
        current_instruction += " loosen"
    elif tuning_instruction[i].isnumeric():  # Check if the character is numeric
        current_instruction += " " + tuning_instruction[i]
        
        j = 1  # Start checking for additional digits
        while True:
            # Check if the next character is out of bounds or not numeric
            if i + j >= len(tuning_instruction) or not tuning_instruction[i + j].isnumeric():
                if current_instruction.strip():  # Ensure we only print if there's something to show
                    print(current_instruction.strip())  # Print the accumulated instruction without leading space

                break  # Exit the while loop
            
            # Append the next numeric character
            current_instruction += tuning_instruction[i + j]
            j += 1  # Move to the next character

        # Update i to skip over the processed digits
        i += j # We subtract 1 because we already incremented i in the for loop

# Print any remaining instruction if not already printed
if current_instruction:
    print(current_instruction)
