# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 28 nov 2024
# ccc '01 j2

def reverse_directions():
    # Read directions until we encounter 'SCHOOL'
    directions = []
    while True:
        instruction = input().strip()
        directions.append(instruction)
        if instruction == 'SCHOOL':
            break
    
    # Process directions in reverse
    # For each turn, we need to output the opposite direction and the previous street
    for i in range(len(directions) - 1, 0, -2):
        turn = directions[i-1]
        street = directions[i-2] if i > 1 else 'HOME'
        
        # Convert R to LEFT and L to RIGHT for the reverse journey:
        if turn == 'R':
            turn = 'LEFT'
        else:
            turn = 'RIGHT'

        if street == 'HOME':
            print(f'Turn {turn} into your HOME.')
        else:
            print(f'Turn {turn} onto {street} street.')
                  
# Run the program
reverse_directions()
