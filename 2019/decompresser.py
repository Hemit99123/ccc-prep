# Hemit Patel
# STUDENT NUMBER
# ICS3U0-1
# Time to Decompress
# INSTRUCTOR NAME
# 29 sep 2024

number_lines = int(input(""));
message_list = []

for _ in range(number_lines):
    coded_message = input("");

    '''
    Learned the .split() function which splits a text into a list based on a specific character in the paramaters. If left empty, it will split the characters based on an empty space given

    But if I were to use , in the paramaters then it would split everytime , was used so I, hemit would become ["I", "hemit"] 
    '''
    coded_message = coded_message.split()

    decoded_message = int(coded_message[0]) * coded_message[1]
    message_list.append(decoded_message)

for message in message_list:
    print(message)
