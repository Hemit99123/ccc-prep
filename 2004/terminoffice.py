# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Terms of Office
# 28 oct 2024

# Input the start and end years
x = int(input(""))
y = int(input(""))

# Loop through each year from x to y inclusive
for year in range(x, y + 1):
    # Check if each role's term lines up with the current year
    # to do this, we subtract the current year by the beggining year.
    # the difference from this should be a multiple of the term served in office 
    # as they should be groupings of that term 
  
    if (year - x) % 3 == 0 and (year - x) % 4 == 0 and (year - x) % 2 == 0 and (year - x) % 5 == 0:
        print("All positions change in year", year)
