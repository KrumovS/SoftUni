cycle = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(cycle):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif current_number <= 399:
        p2 += 1
    elif current_number <= 599:
        p3 += 1
    elif current_number <= 799:
        p4 += 1
    elif current_number > 799:
        p5 += 1

p1_percent = p1 / cycle * 100
p2_percent = p2 / cycle * 100
p3_percent = p3 / cycle * 100
p4_percent = p4 / cycle * 100
p5_percent = p5 / cycle * 100

print(f'{p1_percent:.2f}%')
print(f'{p2_percent:.2f}%')
print(f'{p3_percent:.2f}%')
print(f'{p4_percent:.2f}%')
print(f'{p5_percent:.2f}%')