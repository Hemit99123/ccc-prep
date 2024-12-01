# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# 29 nov 2024
# ccc j2 2004

start = int(input("Enter the start year: "))  # The year when the positions first change
end = int(input("Enter the end year: "))      # The last year in the range we want to check

# We know that all positions change every 60 years (LCM of 4, 2, 3, and 5) The years that the different city position changes 
# LCM is used because that finds a number that all the numbers can easily divide into, meaning 
# that an equal amount of position changes has occured in ALL of different positions 
# Even though they change at different years.

cycle_period = 60  # This is the interval after which all positions change again

# The start year is the first year when all positions change
# Therefore, we need to find all subsequent years that are multiples of 60 from the start year

# Loop through all years between start and end (inclusive)
for year in range(start, end + 1):  # The loop checks each year from 'start' to 'end'
    # Check if the difference between the current year and the start year is a multiple of 60
    # If (year - start) is divisible by 60, it means this year is an interval of 60 years from the start year.
    if (year - start) % cycle_period == 0:
        # If the condition is met, print the year where all positions change
        # This is because this year is a multiple of 60 from the start year.
        print(f"All positions change in year {year}")
