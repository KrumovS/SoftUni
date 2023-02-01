num = int(input())

for i in range(1111, 10000):
    for index, digit in enumerate(str(i)):
        if int(digit) != 0 and num % int(digit) == 0:
            magic_number = True
        else:
            magic_number = False
            break
    if magic_number:
        print(f'{i}', end=" ")


