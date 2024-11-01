# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# CCC 2011 Contest J2
# 31 oct 2024


first = int(input())
second = int(input())

sequence = [first, second]

count = 0

while True:
    if (sequence[count] < sequence[count + 1]):
        break
    difference = sequence[count] - sequence[count+1]
    sequence.append(difference)
    count += 1

print(len(sequence))
