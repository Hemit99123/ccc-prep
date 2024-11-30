# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# 29 nov 2024
# mock ccc 23 j3 contest 1 dmoj

user_input = input().split()

n = user_input[0]
k = user_input[1]
m = user_input[2]

a = input().split()
b = input().split()


boundle_count = 0

for i in range(len(a)):
    for j in range(len(b)):
        if (int(a[i]) + int(b[j]) == int(m) and abs(i-j) >= int(k)):
            boundle_count += 1

print(boundle_count)
