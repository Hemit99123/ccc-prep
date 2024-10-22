# Hemit Patel
# 781159
# ICS3U0-4
# MR VEERA
# 22 oct 2024
# problem: tudor drinks coffee

# the content in each part of the straw (either tapioca or tea)

content_straw_1 = input()
content_straw_2 = input()
content_straw_3 = input()
content_straw_4 = input()
content_straw_5 = input()

# a counter to keep track of amount of tapioca 
count_tapioca = 0

# wrote the target for the next conditional statements to avoid redudncy
# also it makes it easier to change what we are comparing in the if statements
# allowing for better maintainability of the codebase

target = "P"

# if the target, that means tapioca is in that part of the straw so INCREMENT by 1 (+=)
if (content_straw_1 == target):
    count_tapioca += 1

if (content_straw_2 == target):
    count_tapioca += 1

if (content_straw_3 == target):
    count_tapioca += 1

if (content_straw_4 == target):
    count_tapioca += 1

if (content_straw_5 == target):
    count_tapioca += 1

print(count_tapioca)
