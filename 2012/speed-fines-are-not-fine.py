# Hemit Patel
# MR VEERA 
# ICS3U0-4
# Oct 19 2024
# CCC '12 J1 - Speed fines are not fine!

limit_speed = int(input())
user_speed = int(input())

difference = user_speed - limit_speed

if (difference <= 0):
  print("Congratulations, you are within the speed limit!")
else:
  if (1 <= difference <=20):
    fine = 100
  elif (21 <= difference <= 30):
    fine = 270
  else: 
    fine = 500

  print(f"You are speeding and your fine is ${fine}.")