# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 22 oct 2024
# problem: championship

program_input = input()

seperated_input = program_input.split()

number_obstacles = int(seperated_input[0])

andrew_jump_height = int(seperated_input[1])
tommy_jump_height = int(seperated_input[2])

andrew_time = 0
tommy_time = 0

for _ in range(number_obstacles):

    obstacles_height = input()

    seperated_input = obstacles_height.split()

    andrew_obstacle = int(seperated_input[0])
    tommy_obstacle = int(seperated_input[1])

    if (andrew_obstacle >= andrew_jump_height):
        andrew_time += 2
    else:
        andrew_time += 1

    if (tommy_obstacle >= tommy_jump_height):
        tommy_time += 2
    else:
        tommy_time += 1


if (andrew_time < tommy_time):
    print("Andrew wins!")

elif (tommy_time < andrew_time):
    print("Tommy wins!")

else:
    print("Tie!")
