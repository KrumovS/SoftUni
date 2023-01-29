import sys

cycle = int(input())

max_number = -sys.maxsize
total_sum = 0

for i in range(cycle):
    current_number = int(input())
    total_sum += current_number

    if current_number > max_number:
        max_number = current_number

if max_number == total_sum - max_number:
    print(f'Yes')
    print(f'Sum = {max_number}')
else:
    diff = abs(total_sum - max_number * 2)
    print(f'No')
    print(f'Diff = {diff}')
