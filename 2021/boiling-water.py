# Hemit Patel
# 781159
# ICS3U0-4 (reorged)
# Boiling point
# Mr Veera
# 3 oct 2024

# The input for the program
temperature = int(input("Enter the temperature in celsius: "))

# Outputs for the programs
pressure = 5 * temperature - 400
sea_level = 0


# Changing the sea level based on different conditions (employing conditional logic)
if pressure < 100:
    sea_level = 1
elif pressure == 100:
    sea_level = 0
elif pressure > 100:
    sea_level = -1


print(f"The sea level is {sea_level} and the pressure is {pressure}.")
