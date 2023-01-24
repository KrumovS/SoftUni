num1 = int(input())
num2 = int(input())
operator = input()

condition = ''
result = 0

if operator == "+":
    result = num1 + num2
    condition = 'odd_or_even'
elif operator == "-":
    result = num1 - num2
    condition = 'odd_or_even'
elif operator == "*":
    result = num1 * num2
    condition = 'odd_or_even'
elif operator == "/":
    if num2 != 0:
        result = num1 / num2
        condition = "result"
    else:
        condition = "result"
elif operator == "%":
    if num2 != 0:
        result = num1 % num2
        condition = "result"
    else:
        condition = "result"
if condition == "odd_or_even":
    if result % 2 == 0:
        print(f'{num1} {operator} {num2} = {result} - even')
    else:
        print(f'{num1} {operator} {num2} = {result} - odd')
elif condition == "result":
    if operator == "/" and num2 != 0:
        print(f'{num1} {operator} {num2} = {result:.2f}')
    elif (operator == "/" or operator == "%") and num2 == 0:
        print(f'Cannot divide {num1} by zero')
    else:
        print(f'{num1} {operator} {num2} = {result:}')





