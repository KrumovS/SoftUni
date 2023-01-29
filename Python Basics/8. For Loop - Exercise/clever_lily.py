lily_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())

toys = 0
money = 0
total_money = 0

for i in range(1, lily_age + 1):
    if i % 2 != 0:
        toys += 1
    else:
        money += 10
        total_money += money - 1

total_money = total_money + toys * toy_price

diff = abs(total_money - washing_machine_price)

if total_money >= washing_machine_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')
