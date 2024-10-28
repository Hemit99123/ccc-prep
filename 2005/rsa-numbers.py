# Hemit Patel
# ICS3U0-4 
# MR VEERA
# 28 oct 2024 
# rsa number

lower_limit = int(input("Enter lower limit: "))
higher_limit = int(input("Enter higher limit: "))

rsa_number_counter = 0

for number in range(lower_limit, higher_limit + 1):
    counter = 2  # Start at 2 to include 1 and the number itself (those will always be divisiable by the number at hand)

    # divisors cannot be higher than the quiotient of number / 2 (int division produces that output)
  
    for divisor in range(2, number // 2 + 1):
        if number % divisor == 0:
            counter += 1
        if counter > 4:
            break  # No need to continue if we already have more than 4 divisors

    if counter == 4:
        rsa_number_counter += 1

print(f"The number of RSA numbers between {lower_limit} and {higher_limit} is {rsa_number_counter}")
