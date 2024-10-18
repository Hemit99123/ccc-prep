# Hemit Patel
# STUDENT NAME
# ICS3U0-1 (Course code)
# J1 2023 Solution
# TEACHER NAME
# 21 sep 2024

# The inputs for the program to work

packages = int(input(""));
collision = int(input(""));

# Providing 50 points per package delivered which is expressed in P

points_gained = packages * 50

# Now we figure out how much points we must lose because of collisons
# We keep it a postive because in the equation we will model it a negative

points_lost = collision * 10

# Subtract the amount of points that need to be lost from our total sum to get accurate score

final_score = points_gained - points_lost

# Now employing conditonal logic to ensure bonus 500 points are earned based on cretrion

if packages > collision:
    final_score += 500

print(final_score)
