# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# Special Day

month = int(input(""))
day = int(input(""))

# The CCC special day in variables to avoid repeating these numbers
# The target_month is Feb and target_day represents the day 18 so its feb 18

target_month = 2 
target_day = 18

month = int(input())
day = int(input())
thirtyone_day_months = [1,3,5,7,8,10,12]
thirty_day_months = [2,4,6,9,11]

# Double checking that months and day is in the proper range 
# (can't have a 13th month) or (can't have a 32nd day)

if (1 <= month <= 12) and (1<= day <= 31):

    # First checking the months because if months are above or below feb
    # It means the day doesn't matter as it is a smaller unit of time

    if (month > target_month):
        print("After")
        
    elif (month < target_month):
        print("Before")
        
    else:

        # In this else statement, we assum that the month == target_month because
        # the other if blocks werent true

        # Now day does matter because months are the same

        if (day > target_day):
            print("After")
        
        elif (day < target_day):
            print("Before")

        # If days are not greater or lesser than it means both the month and day
        # are equal to eachother
    
        else:
            print("Special")

# Returning an error if not given a proper month/day in the range

else:
    print("Not a valid month/day")