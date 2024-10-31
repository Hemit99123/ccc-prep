# Hemit Patel
# 781159
# MR VEERA
# ICS3U0-4
# 30 oct 2024 
# deal or no deal

def isDeal():
    number_opened = int(input())

    dollar_amounts = {
        1: 100,
        2: 500,
        3: 1000,
        4: 5000,
        5: 10000,
        6: 25000,
        7: 50000,
        8: 100000,
        9: 500000,
        10: 10000000,
    }
    
    unopened_cash = 10691600
    counter = 0

    # Loop through the number of opened briefcases
    while counter < number_opened:
        counter += 1
        opened = int(input())
        unopened_cash -= dollar_amounts[opened]

    banker_offer = int(input())

    # Calculate the number of unopened briefcases
    unopened_count = 10 - number_opened

    # Calculate the average of the remaining amounts
    avg = unopened_cash / unopened_count
    
    # Compare the banker's offer with the average
    if banker_offer > avg:
        return "deal"
    else:
        return "no deal"


print(isDeal())
