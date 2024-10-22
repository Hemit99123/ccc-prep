# Hemit Patel
# 781159
# ICS3U0-4 
# MR VEERA
# Unstable 
# 21 oct 2024

'''
Problem Statement: Substance Stability Classification
You are developing a program to assess the stability of a chemical substance based on its temperature in degrees Celsius. The stability classification is based on the following criteria:

Highly Unstable: The substance is at a temperature less than 0 degrees.
Unstable: The temperature is at least 0 but below 25 degrees.
Stable: The temperature is from 25 degrees up to 75 degrees.
Moderately Stable: The temperature is greater than 75 but less than or equal to 100 degrees.
Decomposed: The temperature exceeds 100 degrees.
Requirements
Ask the user to enter the temperature of the substance.
Implement conditional statements to determine the stability classification of the substance.
Include error handling to ensure that the input is a valid number.
Print a message indicating the stability classification based on the input.
Example Output
Input: -5 → Output: The substance is Highly Unstable.
Input: 10 → Output: The substance is Unstable.
Input: 50 → Output: The substance is Stable.
Input: 90 → Output: The substance is Moderately Stable.
Input: 110 → Output: The substance is Decomposed.
Input: abc → Output: Please enter a valid number.
'''


temperature = int(input("Enter the temperature"))

if (temperature < 0):
    print("Highly Unstable")

elif (0 <= temperature < 25):
    print("Unstable")

elif (25 <= temperature <= 75):
    print("Stable")

elif (75 <= temperature <= 100):
    print("Moderately Stable")

else:
    print("Decomposed")
