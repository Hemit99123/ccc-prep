# Hemit Patel
# STUDENT NAME
# ICS3U0-1 (Course code)
# J1 2023 Solution
# TEACHER NAME
# 21 sep 2024

def Solution():
  n = int(input(""))
  sum = 0
  
  ref = {
    "poblano": 1500,
    "mirasol": 6000,
    "serrano": 15500,
    "cayenne": 40000,
    "thai": 75000,
    "habanero": 125000
  }

  for _ in range(n):
    p = input("")
    p = p.lower()

    if p not in ref:
      return "Invalid pepper"

    sum += ref[p]
    

  return sum

print(Solution())
