# Hemit Patel
# STUDENT NAME
# ICS3U0-1 (Course code)
# J1 2016 Solution
# TEACHER NAME
# 21 sep 2024

def Solution():
    wins = 0

    for i in range(6):
        win_or_loss = input('')

        if win_or_loss == "W":
            wins += 1

    if wins == 5 or wins == 6:
        return 1
    elif wins == 3 or wins == 4:
        return 2
    elif wins == 1 or wins == 2:
        return 3
    else:
        return -1

print(Solution());
