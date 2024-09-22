# Hemit Patel
# STUDENT NAME
# ICS3U0-1 (Course code)
# J1 2023 Solution
# TEACHER NAME
# 21 sep 2024

# The inputs for the program to work

P = int(input(""));
C = int(input(""));
F = 0;

# Providing 50 points per package delivered which is expressed in P

F = P * 50

# Now we figure out how much points we must lose because of collisons

points_lost = C * 10

# Subtract the amount of points that need to be lost from our total sum to get accurate score

F = F - points_lost

# Now employing conditonal logic to ensure bonus 500 points are earned based on cretrion

if P > C:
    F += 500

print(F)
