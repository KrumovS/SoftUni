number = int(input())

even_number = 0
odd_number = 0

for i in range(number):
    current_number = int(input())
    if i % 2 == 0:
        even_number += current_number
    else:
        odd_number += current_number

differance = abs(even_number-odd_number)

if even_number == odd_number:
    print(f'Yes')
    print(f'Sum = {even_number}')
else:
    print(f'No')
    print(f'Diff = {differance}')