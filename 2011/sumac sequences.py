# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# CCC 2011 Contest J2
# 31 oct 2024

# getting the first 2 values of the sequences
first = int(input())
second = int(input())

# adding to the sequence
sequence = [first, second]

# this count will be used to keep reference (pointer) as to the index position being 
# accessed within the loop itself
count = 0

# infinite loop because we do not know when there will be an end

while True:
    # here we check for a sentinel of if the current pointer is less than the next value
    # if so we break out of the loop because the sequence has officially ended
    
    if (sequence[count] < sequence[count + 1]):
        break
    # otherwise continue on with the logic, no need for else because the break would 
    # stop all logic within the loop body
    
    # we find the difference that we will use as the next value based on the current pointer 
    # and the next value
    
    difference = sequence[count] - sequence[count+1]
    # add that to our collection of numbers
    sequence.append(difference)
    count += 1

# len() function will print out the number of items within a list and since 
# this list contains all the values for the sequence it would find all 
# numbers within the sequence

print(len(sequence))
