# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# 29 nov 2024
# ccc j2 2004


# USES MATH CONCEPTS LIKE LCM 

start = int(input())
end = int(input())

common_quotient = start % 60

for year in range(start,end+1):
    if (year % 60 == common_quotient):
        print(f"All positions change in year {year}")
