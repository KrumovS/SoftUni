balance = 0

while True:
    money = input()

    if money == 'NoMoreMoney':
        break
    elif float(money) > 0:
        print(f'Increase: {float(money):.2f}')
        balance += float(money)
    elif float(money) <= 0:
        print(f'Invalid operation!')
        break

print(f'Total: {balance:.2f}')


