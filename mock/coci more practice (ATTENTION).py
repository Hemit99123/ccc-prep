# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# COCI Contest 1 #2
# 18 nov 2024

input_1 = input().split()

num_chocolates = int(input_1[0])
queries = int(input_1[1])

costs = input().split()

print(costs)

luna = 0
fran = 0

for _ in range(queries):
    query = input().split()
    max_price = int(query[0])
    num_chocolates_bought = int(query[1])

    for index in range(num_chocolates_bought):
        print(index)
        cost = int(costs[index])

        if (cost <= max_price):
            luna += cost
        else:
            fran += cost - max_price
            luna += max_price

print(luna-fran)
            
        
