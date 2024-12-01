# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# 29 nov 2024
# ccc j2 2004

start = int(input())
end = int(input())

common_remainder = start % 60

for year in range(start,end+1):
    if (year % 60 == common_remainder):
        print(f"All positions change in year {year}")
