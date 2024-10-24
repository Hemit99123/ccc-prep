# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# fruit market pricing 
# 24 oct 2024

'''
Problem: Fruit Market Pricing
You are tasked with creating a program for a fruit market that applies different pricing rules based on the quantity of fruit purchased. The pricing rules are as follows:

If a customer buys fewer than 5 pieces of fruit, each piece costs $2.
If a customer buys 5 to 10 pieces of fruit (inclusive), each piece costs $1.50.
If a customer buys more than 10 pieces of fruit, each piece costs $1.
If the customer buys 20 or more pieces of fruit, they receive an additional discount of 10% on the total cost.
If the quantity is negative or zero, print "Invalid quantity. Please enter a positive number."
Input:
An integer representing the number of pieces of fruit purchased.
Output:
The total cost for the customer, formatted to two decimal places.


'''
quantity = int(input("Enter the quantity:"))

if (quantity <= 0):
    print("Invalid quantity. Please enter a postive number.")
else:
    # we need a nested if because the output of total cost
    # should not be outputted if quantity is 0 or below

    # here we check for the quantity and the corresponding price
    # no need to initialize variable cost_per prior hand because
    # it will be assigned during the if statement execution
    
    if (quantity < 5):
        cost_per = 2
    elif (5 <= quantity <= 10):
        cost_per = 1.50
    elif (quantity > 10):
        cost_per = 1
        
    cost = quantity * cost_per

    if (quantity >= 20):
        cost = cost - (cost * 0.1)

    print("Total cost:", cost)


