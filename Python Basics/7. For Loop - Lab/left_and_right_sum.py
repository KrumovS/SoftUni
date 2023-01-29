number = int(input())

differance = 0
total_sum1 = 0
total_sum2 = 0
p = 0

for i in range(number * 2):
    p += 1
    current_number = int(input())
    if p > number:
        total_sum1 += current_number
    else:
        total_sum2 += current_number

differance = abs(total_sum1 - total_sum2)

if differance == 0:
    print(f'Yes, sum = {total_sum1}')
else:
    print(f'No, diff = {differance}')
