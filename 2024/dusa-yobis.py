# Hemit Patel
# 781159
# ICS3U0
# MR VEERA
# CCC J2 2024
# 1 dec 2024 

# Input for the size of Dusa
dusa_size = int(input())

# Input for the initial Yobi size
yobi_size = int(input())

# Keep running the loop as long as Dusa is larger than Yobi
while (dusa_size > yobi_size):
    # Dusa eats the Yobi and increases in size
    dusa_size += yobi_size
    
    # Input for the next Yobi size (updaates the yobi_size variable as well for the loop condition)
    yobi_size = int(input())

# Output the final size of Dusa when it runs away
print(dusa_size)
