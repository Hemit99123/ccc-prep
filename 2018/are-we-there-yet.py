# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# 30 oct 2024
# are we there yet

distances = map(int, input().split())
positions = [0]


for i in distances: 
    positions.append(positions[-1] + i)

for i in range(5):
    for j in range(5):
        
        distances = positions[i] - positions[j]
        
        if (distances < 0):
            distances *= -1
            
        print(f"{distances} ", end="")

    # print an empty line to create a one space gap
    print()
