# Hemit Patel
# STUDENT NAME
# ICS3U0-1 (Course code)
# J3 2021 Solution
# INSTRUCTOR NAME
# 22 sep 2024

# The previous direction in case we get 0 for the first 2 numbers sum

prev = ""

# Keep it running infinitely because there is no set amount of inputs

while True:
    
    N = input("");

    # This signals the end of the input so break out for the while loop
    
    if N == "99999":
        break;

    # Convert to the list so we can take on this problem number by number based on indexes (0-4)
    
    N = list(N);

    # We are employing this logic here where the 0 index is the first number and the 1 index is the second number
    
    S = int(N[0]) + int(N[1]);
    direction = "";
    
        
    # Employing conditional logic to see if the number is a odd/even (calc its remainder with %)
    # Using this odd/even state to determine the direction we go too
    # If the sum is 0 then use the previous direction (the else statement)

    if S % 2 == 1:
        direction = "left";

    elif S % 2 != 1 and S != 0:
        direction = "right";

    else:
        direction = prev

    # Assigning the new outcome for direction
    
    prev = direction

    # The amount of steps (last 3 numbers) concated as they should not be mathematically added up
    steps = N[2] + N[3] + N[4]
    
    print(direction + " " + steps)
    
    
