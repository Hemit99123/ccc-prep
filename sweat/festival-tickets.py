# Hemit Patel
# 781159
# ics3u0-4
# festival ticket pricing calculator
# oct 18 2024
# mr veera


age = int(input("Enter your age:"))

# .lower() will lowercase all the characters so that case senstivity does not matter as long as
# everything being checked is IN LOWERCASE FORMAT

purchase_method = input("Enter your purchase method as either door or advance:").lower()

# Checking which purchase method is being used to employing nested if statements to get the price

if (purchase_method == "door"):

    # Going in a consistent range so that the age ranges are accurately compared (asc order)
    # all inclusive because the next number is the lower limit for the next range
    
    if (age <= 12):
        ticket_price = 7
    elif (13 <= age <= 17):
        ticket_price = 15
    elif (18 <= age <= 64):
        ticket_price = 20
    else:
        ticket_price = 12
        
    print(f"Ticket price: ${ticket_price}")

elif (purchase_method == "advance"):

    if (age <= 12):
        ticket_price = 5
    elif (13 <= age <= 17):
        ticket_price = 10
    elif (18 <= age <= 64):
        ticket_price = 15
    else:
        ticket_price = 10
    print(f"Ticket price: ${ticket_price}")

# If none of these methods are true, it means its an invalid input so output an error

else:
    print("The purchase method can either be a door or advance only!")

