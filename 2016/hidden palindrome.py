# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 1 nov 2024

# Input a word and convert it into a list of characters
word = list(input(""))
possible_palindromes = []

# Loop to generate all possible substrings
for start in range(len(word)):
    for end in range(start + 1, len(word) + 1):
        # Get the substring from 'start' to 'end'
        substring = word[start:end]
        
        # Check if the substring is a palindrome
        if substring == substring[::-1]:
            possible_palindromes.append("".join(substring))

max_value = len(list(possible_palindromes[0]))

word_output = ""

for palindrome in possible_palindromes:
    if (len(list(palindrome)) > max_value):
        max_value = len(list(palindrome))

print(max_value)    
