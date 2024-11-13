# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# ccc 04 j3 
# 12 nov 2024

number_adj = int(input())
number_nouns = int(input())
total = number_adj + number_nouns

adj_list = []
nouns_list = []

for _ in range(number_adj):
    adj = input()
    adj_list.append(adj)

for _ in range(number_adj, total):
    noun = input()
    nouns_list.append(noun)
    
for adj in adj_list:
    for noun in nouns_list:
        print(f"{adj} as {noun}")
