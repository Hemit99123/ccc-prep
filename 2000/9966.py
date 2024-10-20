# Hemit Patel
# MR VEERA 
# ICS3U0-4
# Oct 20 2024
# CCC '00 - J2 9966

# Dictionary for digit rotations
# A dict models a key-value relationship where the key is associated with some sort of value
# In our case, they key is the digit and the value is the digit rotated by 180 deg
rotated_digits = {"1": "1", "8": "8", "6": "9", "9": "6", "0": "0"}

low = int(input())
high = int(input())

# Initialize counter for rotatable numbers
amount = 0

# Iterate through every number in the range [a, b]
for number in range(low, high + 1):
    number_str = str(number)  # Convert the number to a string so we can iterate through digits
    rotated = ""  # Initialize an empty string to build the rotated number
    is_rotatable = True  # Flag to check if the number is valid when rotated

    # Iterate through each digit in the number
    for digit in number_str:
        # Check if the digit can be rotated
        if digit in rotated_digits:
            rotated = rotated_digits[digit] + rotated  # Build the rotated number by setting the rorated variable to the rotated digit + previous digits from before (+rotated)
        else:
          # MAKING ALGORITHM MORE EFFIENCT BY USING BREAK STATEMENT
            is_rotatable = False  # If digit can't be rotated, mark the number as invalid
            break  # Stop further checking for this number as it's not rotatable because it doesn't have a rotatable number meaning the whole number will not look the same

    # If the number is rotatable and matches the original number after rotation
    if rotated == number_str:
        amount += 1  # Increment the counter if the rotated number equals the original

# Output the count of valid rotatable numbers
print(amount)
