# Hemit Patel
# STUDENT NUMBER
# ICS3U0-1 
# Cold Compressor
# INSTRUCTOR NAME 
# 29 sep 2024

number_lines = int(input(""))

list_score = []

for _ in range(number_lines):
    decoded = input("")
    decoded = list(decoded)
    decoded_len = len(decoded)

    if decoded_len == 0:
        continue  # Skip empty input

    prev = decoded[0]
    count = 1  # Initialize count to 1 since we are already counting the first character
    output = ""

    for i in range(1, decoded_len):  
        if decoded[i] != decoded[i - 1]:
            output += f'{count} {decoded[i - 1]} '
            count = 1
        else:
            count += 1

    # Handle the final group of characters after the loop as it isn't shown
    output += f'{count} {decoded[-1]}'

    print(output)
