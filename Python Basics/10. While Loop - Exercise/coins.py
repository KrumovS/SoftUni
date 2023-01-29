change = float(input())
change = int(change * 100)

coin_counter = 0

while change > 0:
    if change // 200 != 0:
        change -= 200
        coin_counter += 1
    elif change // 100 != 0:
        change -= 100
        coin_counter += 1
    elif change // 50 != 0:
        change -= 50
        coin_counter += 1
    elif change // 20 != 0:
        change -= 20
        coin_counter += 1
    elif change // 10 != 0:
        change -= 10
        coin_counter += 1
    elif change // 5 != 0:
        change -= 5
        coin_counter += 1
    elif change // 2 != 0:
        change -= 2
        coin_counter += 1
    else:
        change -= 1
        coin_counter += 1

print(coin_counter)