# Hemit Patel
# STUDENT NUMBER
# ICS3U0-1 
# Bronze Count
# INSTRUCTOR NAME 
# 28 sep 2024

total_participants = int(input(""))


list_scores = []

for _ in range(total_participants):
  score = int(input(""))

  list_scores.append(score)

sorted_list = sorted(set(list_scores), reverse=True)

bronze_winners = 0

for i in list_scores: 
  if i == sorted_list[2]: 
    bronze_winners += 1 

print(sorted_list[2], bronze_winners)
