# Hemit Patel
# ICS3U0-4 
# MR VEERA
# 28 oct 2024 
# magic squares

# we split the input so that it puts them into a list so we can access each of those integers one at a time 
# note; these integers are in string form so they must be converted into a int using int() type casting for 
# arthemtic operations 

row1 = input().split()
row2 = input().split()
row3 = input().split()
row4 = input().split()

# must be in the same index of each row, so we are creating a new list with those elements using indexing []

column1 = [row1[0], row2[0], row3[0], row4[0]]
column2 = [row1[1], row2[1], row3[1], row4[1]]
column3 = [row1[2], row2[2], row3[2], row4[2]]
column4 = [row1[3], row2[3], row3[3], row4[3]]


# sums of the rows (counter)
sum_row1 = 0
sum_row2 = 0
sum_row3 = 0
sum_row4 = 0

# sums of the cols (counter)
sum_col1 = 0
sum_col2 = 0
sum_col3 = 0
sum_col4 = 0

# iterating over the different rows and columsn to get the sum 

for element in row1:
  sum_row1 += int(element)
for element in row2:
  sum_row2 += int(element)
for element in row3: 
  sum_row3 += int(element)
for element in row4:
  sum_row4 += int(element)

for element in column1:
  sum_col1 += int(element)
for element in column2:
  sum_col2 += int(element) 
for element in column3:
  sum_col3 += int(element)
for element in column4:
  sum_col4 += int(element)

# the sum of all these different rows and columns MUST be the same so we are checking for it here
# if they are then you truly have a magic sqaure

if (sum_row1 == sum_row2 == sum_row3 == sum_row4 == sum_col1 == sum_col2 == sum_col3 == sum_col4):
  print("magic")
else:
  print("not magic")