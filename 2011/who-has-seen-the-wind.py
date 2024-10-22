# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA 
# Who has seen the wind j2 2011


humidity = int(input())
max_hours_waited = int(input())
hours = 1

while True:
    if (hours == max_hours_waited):
        print("The balloon does not touch ground in the given time.")
        break

    altitude = -6 * hours ** 4 + humidity * hours ** 3 + 2 * hours ** 2 + hours

    if (altitude <= 0):
        print("The balloon first touches ground at hour:")
        print(hours)
        break

    hours += 1