# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# Special Day

month = int(input(""))
day = int(input(""))


# The CCC special day in variables to avoid repeating these numbers
# The 2 is Feb and 18 represents the day 18 so its feb 18

target_month = 2 
target_day = 18

# Checking if the current date info is before, after or on these special days

# < means less than so this is before because the month/day would be LOWER

if (month < target_month and day < target_day):
    print("Before")

# The opposite of the above if block

elif (month > target_month and day > target_day):
    print("After")

elif (month < target_month and day > target_day):
    print("Before")

elif (month > target_month and day < target_day):
    print("After")

elif (month == target_month and day < target_day):
    print("Before")

elif (month < target_month and day == target_day):
    print("Before")

elif (month > target_month and day == target_day):
    print("After")

elif (month == target_month and day > target_day):
    print("After")

# Otherwise it must be on the day so therefore output "Special"

else:
    print("Special")


## BETTER SOLUTION -> LEARN IT AND COMMENT ##

month = int(input())
day = int(input())
thirtyone_day_months = [1,3,5,7,8,10,12]
thirty_day_months = [2,4,6,9,11]

if (1 <= month <= 12) and (1<= day <= 31):
    if (month > 2):
        print("After")
        
    elif (month < 2):
        print("Before")
        
    else:
        if (day > 18):
            print("After")
        
        elif (day < 18):
            print("Before")
            
        else:
            print("Special")