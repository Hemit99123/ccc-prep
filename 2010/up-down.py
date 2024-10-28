a = int(input())
b = int(input())
c = int(input())
d = int(input())
s = int(input())

# Calculate total steps for Nikky
cycle_nikky = a + b
complete_cycles_nikky = s // cycle_nikky
remaining_steps_nikky = s % cycle_nikky

steps_nikky = complete_cycles_nikky * (a - b)
if remaining_steps_nikky <= a:
    steps_nikky += remaining_steps_nikky
else:
    steps_nikky += a - (remaining_steps_nikky - a)

# Calculate total steps for Byron
cycle_byron = c + d
complete_cycles_byron = s // cycle_byron
remaining_steps_byron = s % cycle_byron

steps_byron = complete_cycles_byron * (c - d)
if remaining_steps_byron <= c:
    steps_byron += remaining_steps_byron
else:
    steps_byron += c - (remaining_steps_byron - c)

# Determine the result
if steps_nikky > steps_byron:
    print("Nikky")
elif steps_byron > steps_nikky:
    print("Byron")
else:
    print("Tied")
