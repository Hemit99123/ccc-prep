# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 2 dec 2024
# ccc '01 j2

# Read directions until we encounter 'SCHOOL'
directions = []

# Adding all directions into a ds called a list
# A list stores all items within an collection 
# and we can retrieve each one of these items

while True:
    instruction = input().strip()
    directions.append(instruction)
    
    # A sential of SCHOOL will end this infinite loop as an infinite loop cannot keep running forever
    # Or else a TLE error would be presented
    
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
                
