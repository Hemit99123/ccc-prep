# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Happy or Sad
# 14 oct 2024

text = input("Enter the text")

# Counting the instances of the emoticons using python builtin .count() functions

happy = text.count(":-)")
sad = text.count(":-(")

# Checking if both happy and sad have none emoticons

if (happy == 0 and sad == 0):
    print("none")

# Happy is less than sad meaning sad has more

elif (happy < sad):
    print("sad")

# Happy has more as > is greater than

elif (happy > sad):
    print("happy")


# If none of these conditions are meant, it means that the amount of happy and sad are equal

else:
    print("unsure")