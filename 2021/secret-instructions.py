# Hemit Patel
# 781159
# ICS3U0-4
# J3 2021 Solution
# Mr Veera
# 29 nov 2024

# The previous direction in case we get 0 for the first 2 numbers sum

prev = ""

# Keep it running infinitely because there is no set amount of inputs until 99999 is inputted

while True:
    
    number = input("");

    # 99999 signals the end of the input so break out for the while loop, it is our sential 
    
    if number == "99999":
        break;

    # We are employing this logic here where the 0 index is the first number and the 1 index is the second number
    # Since the number is NOT an integer but rather a string, we can use index values to get each character (numeral in our case)
    
    sum_first_2 = int(number[0]) + int(number[1]);
    direction = "";
    
        
    # Employing conditional logic to see if the number is a odd/even (calc its remainder with %)
    # Using this odd/even state to determine the direction we go too
    # If the sum is 0 then use the previous direction (the else statement)

    if sum_first_2 % 2 == 1:
        direction = "left";

    elif sum_first_2 % 2 != 1 and sum_first_2 != 0:
        direction = "right";

    else:
        direction = prev

    # Assigning the new outcome for direction
    
    prev = direction

    # The amount of steps (last 3 numbers) concated as they should not be mathematically added up
    steps = number[2] + number[3] + number[4]
    
    print(direction + " " + steps)
    
    
