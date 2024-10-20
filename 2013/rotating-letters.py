# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA 
# Rotating Letters 
# 20 oct 2024

word = input()

# made a list of all allowed values which can be rotated
allowed = ["I", "O", "S", "H", "Z", "X", "N"]

# default output will be yes unless a letter from the word is not in allowed
output = "YES"

# iterating through word to get each character

for letter in word:
    # so if the letter is not in the list of allowed change output to no 
    # because this word will not be the same rotated
    # and break function as it will never be able to be the same rotatated forever due to this one ill-fated letter

    if (letter not in allowed):
        output = "NO"
        break;

# here we print the output whether that is yes or no
print(output)