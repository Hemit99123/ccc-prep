# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 2 dec 2024
# ccc '01 j2

# Read directions until we encounter 'SCHOOL'
directions = []

while True:
    instruction = input().strip()
    directions.append(instruction)
    if instruction == 'SCHOOL':
        break
    
# Process directions in reverse
# For each turn, we need to output the opposite direction and the previous street
for index_pos in range(len(directions) - 1, 0, -2):
    turn = directions[index_pos-1]
    street = directions[index_pos-2] if index_pos > 1 else 'HOME'
        
    # Convert R to LEFT and L to RIGHT for the reverse journey:
    if turn == 'R':
        turn = 'LEFT'
    else:
        turn = 'RIGHT'

    if street == 'HOME':
        print(f'Turn {turn} into your HOME.')
    else:
        print(f'Turn {turn} onto {street} street.')
                
