# Initialize variables
content_1 = input()
content_2 = input()
content_3 = input()
content_4 = input()
content_5 = input()
content_6 = input()
content_7 = input()

# Store input in a list for easier iteration
contents = [content_1, content_2, content_3, content_4, content_5, content_6, content_7]

counter = 0

# Iterate through the list and count chunks
for i in range(7):
    if contents[i] == "J" and (i == 0 or contents[i - 1] != "J"):
        counter += 1

print(counter)
