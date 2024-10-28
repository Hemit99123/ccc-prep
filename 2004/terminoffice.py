# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# Terms of Office
# 28 oct 2024

# Input the start and end years
year_started = int(input(""))
year_ended = int(input(""))

# Loop through each year from x to y inclusive
# to make it inclusive we must add 1 to the higher limit because python discludes that in its computation 
# using the python complier 

for year in range(x, year_ended + 1):
    # Check if each role's term lines up with the current year
    # to do this, we subtract the current year by the beggining year.
    # the difference from this should be a multiple of the term served in office 
    # as they should be groupings of that term 
  
    if (year - year_started) % 3 == 0 and (year - year_started) % 4 == 0 and (year - year_started) % 2 == 0 and (year - year_started) % 5 == 0:
        print("All positions change in year", year)
