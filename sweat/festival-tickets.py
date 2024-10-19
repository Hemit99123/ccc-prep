# Hemit Patel
# 781159
# ics3u0-4
# festival ticket pricing calculator
# oct 18 2024
# mr veera


age = int(input("Enter your age:"))

purchase_method = input("Enter your purchase method as either door or advance:").lower()

ticket_price = 0

if (purchase_method == "door"):

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
        
else:
    print("The purchase method can either be a door or advance only!")

