# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA 
# 781159
# harvest waterloo

## STILL IN PROgress!! ##

amount_rows = int(input())
amount_cols = int(input())

rows = []

for _ in range(amount_rows):
    new_row = input()
    rows.append(new_row)

start_rows = int(input())
start_cols = int(input())

target_rows = rows[:start_rows]

total = 0


for row in target_rows:
    for item in row:

      if (not row.index(item) <= start_cols):
          continue
      elif (item == "S"):
          total += 1
      elif (item == "M"):
          total += 5
      elif (item == "L"):
          total += 10
      else:
        break

print(total)
