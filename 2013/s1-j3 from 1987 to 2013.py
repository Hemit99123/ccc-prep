# Hemit Patel
# 781159
# MR VEERA
# ICS3U0-4
# 26 nov 2024
# ccc 13 s1

year = int(input("Enter the year:"))

while True:
    year += 1
    year_str = str(year)
    is_distinct = True
    
    # Compare each digit with every other digit after it
    for (idx in range(len(year_str))):
        for (next_idx in range(idx + 1, len(year_str))):  # Fixed range here
            if (year_str[idx] == year_str[next_idx]):
                is_distinct = False
                break
                
    if (is_distinct == True):
        print(year)
        break
        
