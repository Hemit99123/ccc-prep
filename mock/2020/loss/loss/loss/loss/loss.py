# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# loss
# oct 21 2024

# The bills for chris
chris_1_bill = int(input())
chris_5_bill = int(input())
chris_10_bill = int(input())
chris_20_bill = int(input())

# The bills for nayaab
nayaab_1_bill = int(input())
nayaab_5_bill = int(input())
nayaab_10_bill = int(input())
nayaab_20_bill = int(input())

# Computing all of the money for both chris and nayaab
total_chris = chris_1_bill + (chris_5_bill * 5) + (chris_10_bill * 10) + (chris_20_bill * 20)
total_nayaab = nayaab_1_bill + (nayaab_5_bill * 5) + (nayaab_10_bill * 10) + (nayaab_20_bill * 20)

# we check if total from chris is greater than total of nayaab
# if so chris must have more money so print his name 

if (total_chris > total_nayaab):
    print("Chris")

# here we check for opposite, if nayaab has more moeny than chris

elif (total_nayaab > total_chris):
    print("Nayaab")

# otherwise we print a tie because they have the same amount of money

else:
    print("Tie")