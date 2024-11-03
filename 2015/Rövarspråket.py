# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA 
# 3 nov 2024
# ccc 15 j3

# for each consonant you have a closest voewl and next consonant in the same index but different list 
# this adds predictiability to our program as for each consonant, it's idx in that list will be the same for clostestVowel and nextConsonant
consonant      = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
closest_vowel   = ['a', 'a', 'e', 'e', 'e', 'i', 'i', 'i', 'i', 'o', 'o', 'o', 'o', 'o', 'u', 'u', 'u', 'u', 'u', 'u', 'u']
next_consonant  = ['c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'z']

word = input()

# we will add the new characters one by one to this variable by using the increment operator +=
# this is outside loop so the value doesn't keep resetting each iteration (repeition of the loop, fancy cs term)

new_word = ""

for char in word:
    # the in operator will check if the character is an item within the list of consonant 
    # since the consonant is a list of all aviable consonant, this will effectively check for if char is a consonant
    # we need to do this so we can ensure that only consonants have the rules of the game applied to it (as speificed in problem set)
    
    if (char in consonant):
        # finding the index in the consonant
        idx = consonant.index(char)
        
        # now we use that same idx for the other lists which will find the corresponding information based on the consonant 
        # as the list was designed as such
        
        new_word += f"{char}{closest_vowel[idx]}{next_consonant[idx]}"
    # if a vowel (non-consonant)
    else:
        # the rules of the game don't apply so just add the character itself (no modifications needed!!!)
        new_word += char

print(new_word)
