# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Q1 Family of 4
# MR VEERA
# 8 oct 2024

# # Ask the user for the age of the youngest child
age_youngest = int(input(""))

# # Ask the user for the age of the second youngest child
age_middle = int(input(""))

# Get the difference between the ages of the youngest and second youngest child
difference = age_middle - age_youngest

# Since difference between ages of all 4 persons are the same we can use it to compute the ages

age_oldest = age_middle + difference

# Printing the output using f"" which combines variables and strings together using {}
print(f"{age_oldest}")