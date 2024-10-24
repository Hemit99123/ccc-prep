# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# ticket pricing
# 24 oct 2024

age = int(input("Enter your age:"))
tickets = int(input("Enter the number of tickets:"))
till_event_days = int(input("Enter the amount of days till the event"))

price = 50

if not (age < 0 and tickets <= 0):
    print("Invalid input. Please enter valid age or ticket quantity")
else:
    
    if (age < 12):
        price = price - (price * 0.5)

    elif (age >= 65):
        price = price - (price * 0.3)

    if (till_event_days > 30):
        price = price - (price * 0.1)
    elif (till_event_days < 3):
        price += 10

    


