import math

figure = input()

if figure == 'square':
    num1 = float(input())
    area = num1 * num1
    print(f'{area:.3f}')

elif figure == 'rectangle':
    num1 = float(input())
    num2 = float(input())
    area = num1 * num2
    print(f'{area:.3f}')

elif figure == 'circle':
    num1 = float(input())
    area = math.pi * num1 ** 2
    print(f'{area:.3f}')

elif figure == 'triangle':
    num1 = float(input())
    num2 = float(input())
    area = (num1 * num2) / 2
    print(f'{area:.3f}')


