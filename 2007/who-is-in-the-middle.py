# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA 
# Who is in the middle 
# 21 oct 2024 

bowl_weight_1 = int(input())
bowl_weight_2 = int(input())
bowl_weight_3 = int(input())

# added everything into a list so we can sort them 
bowl_list = [bowl_weight_1, bowl_weight_2, bowl_weight_3]

# the sorted() function sorts elements from least to greatest values
bowl_list = sorted(bowl_list)

# we take the second value (index 1 because index starts at 0) because that would be the middle value 
# there are only 3 values in the list and if it is least to greatest the 
# the 2nd value would be the middle one
print(bowl_list[1])