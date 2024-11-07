# Hemit Patel
# 781159
# Double Dice
# Mr VEERA
# 15 oct 2024

amount_rolls = int(input())
antonia_score = 100
david_score = 100

counter = 0

while (counter <= amount_rolls):
    rolls = input()
    rolls_list = rolls.split()
    rolls_antonia = int(rolls_list[0])
    rolls_david = int(rolls_list[1])

    if (rolls_antonia < rolls_david):
        antonia_score -= rolls_david

    elif (rolls_antonia > rolls_david):
        david_score -= rolls_antonia

    counter += 1
    
print(antonia_score)
print(david_score)
        
        
