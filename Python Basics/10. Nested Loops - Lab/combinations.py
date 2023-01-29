number = int(input())
counter = 0

for n1 in range (0, number + 1):
    for n2 in range (0, number + 1):
        for n3 in range (0, number + 1):
            if n1 + n2 + n3 == number:
                counter += 1

print(counter)