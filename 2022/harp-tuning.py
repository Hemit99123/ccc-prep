# Hemit Patel
# 781159
# ICS3UO-1
# Harp Tuning Convertor
# Mr. Veera
# 17 dec 2024

tuning_instruction = input("Enter harp tuning instruction:")

# This variable keeps track of the current HUMAN READABLE instruction
# the contents will vary throughout the program because it is wiped
# every time, we are at the "end" of one instruction

current_instruction = ""

# These are strings that are set for cross referencing
# Different cahracters within the tuning instructions"

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# The instructions are in string format so add the
#numerical values in string form

numbers = "0123456789"

# Loop through each character in the tuning instruction
# We loop through based on a counter which acts as the index
# This way, we can find the next value within the string as well
# Simply by adding one to the current position which is index (idx)

# NOTE!! Range counter starts at 0 just like idx val

for idx in range(len(tuning_instruction)):

    character = tuning_instruction[idx]

    # Since index value starts count at 0,it ends one value before length
    # which starts counting from 1 and so on
    # therefore, if you have a length of 10: the final index value would be 9

    # So to check if we are at the end of the string (which would be when we reach the length)
    # We can just add 1 to the idx value because len() and index pos start counting
    # at different times
    
    is_end = idx + 1 == len(tuning_instruction) 

    # Here we check if the character is + or -
    # These values are translated into their word forms of tighten and loosen
    
    if character == "+":
        
        current_instruction += " tighten "
        
    elif character == "-":
        
        current_instruction += " loosen "

    # If it is any other character, no need for translation so add it
    # It will either be a alphabetical or numerical value
    
    else:
        
        current_instruction += character

    # This if conditions checks to see if this is the end to the current instruction
    # If so we print the instruction and wipe the current_instruction variable
    # so we can start off from scratch

    # I noticed a pattern that determines the end of a instruction
    # At the end of an instruction, the current value is a number
    # It also should be the end of the current instruction if we are the end of the command
    # That is what the is_end variable checks for

    # Therefore, either we are at the end of the string or
    # the next character is within the alphabets and current character is a number!


    # I did not put tuning_instruction[idx+1] in a variable because then if we are at the end
    # It would cause a index out of range error as the variable would try finding the index value
    # prior to checking if we are at the end of the input given by user
    
    # By putting it directly within the if clause (after or bool operator) we ensure it is only computed
    # If we know we are not the end of the string and therefore there IS a next value to reference
    # + we only use it once therefore no point in wasting memory space assigning a variable
    
    if (is_end == True) or (tuning_instruction[idx+1] in alphabet and character in numbers):

        print(current_instruction)
        current_instruction = ""

