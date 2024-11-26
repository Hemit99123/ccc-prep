# Hemit Patel
# STUDENT NUMBER 
# ICS3U0-1
# Cold Compressor
# INSTRUCTOR NAME 
# 29 sep 2024 

number_lines = int(input("")) 
list_score = []

for _ in range(number_lines): 
    decoded = input(" ")  # Get the input string
    count = 1  # Start count at 1 for the first character
    output = ""  # This will store the final output

    # Loop through the string starting from the second character
    
    #We start this logic from the second character because we are checking
    # the previous index but the first character does not have a previous index to
    #refer too
    
    for i in range(1, len(decoded)):  
        if decoded[i] != decoded[i - 1]:  # If current character is different from the previous
            output += f'{count} {decoded[i - 1]} '  # Append the count and the previous character to the output
            count = 1  # Reset count for the new character
        else:
            count += 1  # Otherwise, just increment the count

    # Handle the final group of characters after the loop
    output += f'{count} {decoded[-1]}'

    print(output)
