# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA 
# ranges for integer
# 21 oct 2024 

user_int = int(input("Enter the integer:"))

if (user_int < 0):
    print("Range A")
elif (0 <= user_int <= 20):
    print("Range B")
elif (20 < user_int <= 40):
    print("Range C")
elif (40 < user_int <= 100):
    print("Range D")
else:
    print("Out of range")