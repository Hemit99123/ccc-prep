# Hemit Patel
# MR VEERA 
# ICS3U0-4
# Oct 19 2024
# CCC '12 J1 - Speed fines are not fine!

limit_speed = int(input())
user_speed = int(input())

# Seeing how many km/h user is above/below speed limit 
difference = user_speed - limit_speed

# if it is below it should be a negative number so we check for that
# it is equal to 0 because 0 means you are at EXACTLY the speed limit which means you arent speeding and still following the law
if (difference <= 0):
  print("Congratulations, you are within the speed limit!")

# otherwise it can only be above so we use else 

else:
  # employing a nested if statement block where we check for the different ranges of how much over we went for the speed
  # we then assign those to the fine variable which is used for the output for the radar
  
  if (1 <= difference <=20):
    fine = 100
  elif (21 <= difference <= 30):
    fine = 270
  else: 
    fine = 500

  print(f"You are speeding and your fine is ${fine}.")
