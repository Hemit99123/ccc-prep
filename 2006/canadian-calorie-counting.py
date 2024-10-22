# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA 
# Canadian Calorie Counting

burger = int(input())
side = int(input())
drink = int(input())
dessert = int(input())

# calories variable which will be incremented by the different choices of food using the syntax += AMOUNT
calories = 0

# Find the right burger and kcals associated for it
# if 4 is pressed for anyone of the choices, no need to do anything as it means not chosen so therefore 0 kcals added

if (burger == 1):
    calories += 461
elif (burger == 2):
    calories += 431
elif (burger == 3):
    calories += 420


# Find the right drink choice and kcals assocaited for it 

if (drink == 1):
    calories += 130
elif (drink == 2):
    calories += 160
elif (drink == 3):
    calories += 118

# Find the right side order choie and kcals associated for it

if (side == 1):
    calories += 100
elif (side == 2):
    calories += 57
elif (side == 3):
    calories += 70

# Find the right dessrt choice and kcals associated for it

if (dessert == 1):
    calories += 167
elif (dessert == 2):
    calories += 266
elif (dessert == 3):
    calories += 75

print(f"Your total Calorie count is {calories}.")