def Solution():
    n = int(input())
    h = {}
    output = ""

    for i in range(n):
        a = input()
        a = list(a)
        for i in range(len(a)):
            day_number = i + 1
            if a[i] == "Y" and day_number in h:
                h[day_number] += 1
            elif a[i] == "Y" and day_number not in h:
                h[day_number] = 1

    max_value = max(h.values())
    for key, value in h.items():
        if value == max_value:
            output = output + str(key) + ","

    return output.rstrip(',')

print(Solution())
