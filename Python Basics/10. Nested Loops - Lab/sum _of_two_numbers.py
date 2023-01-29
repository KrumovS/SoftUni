num1 = int(input())
num2 = int(input())
magic_number = int(input())

combination = 0
result = 0

flag = False

for i in range(num1, num2 + 1):
    for p in range(num1, num2 + 1):
        result = i + p
        combination += 1
        if result == magic_number:
            flag = True
            break
    if flag:
        break
if flag:
    print(f'Combination N:{combination} ({i} + {p} = {result})')
else:
    print(f'{combination} combinations - neither equals {magic_number}')