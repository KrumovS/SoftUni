word = input()
total_number = 0

for i in word:
    if i == "a":
        total_number += 1
    elif i == "e":
        total_number += 2
    elif i == "i":
        total_number += 3
    elif i == "o":
        total_number += 4
    elif i == "u":
        total_number += 5

print(total_number)
