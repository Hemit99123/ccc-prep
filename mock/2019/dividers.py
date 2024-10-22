# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA 
# Dividers 
# 21 oct 2024 

# Keeping in a string because both integers are inputted in one line meaning there is a space as well 
# so that would make the whole thing a string as spaces aren't allowed in int

two_int = input()

# here we employ the split() function which seperates entities within a string based on a speific character given as input
# in our case we put nothing which means a space, so every space the entities would append to the list

seperated_int = two_int.split()

# now using this list, we use the index to get the 2 numbers and do the nesscary calculation 
# in our case, we want to ensure that the divison can be done evenly, so we use mod 
# if the mod (remainder) is 0 you can perfectly divide into the value 

if (int(seperated_int[1]) % int(seperated_int[0]) == 0):
    print("Hooray! The cookies can be distributed evenly!")

# there is only one other scanrio if not which is cannot distribute/divide evenly!

else:
    print("Boo! The cookies cannot be distributed evenly :(")