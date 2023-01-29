destination = input()
vacation_money = float(input())

money = 0

while destination != "End":
    saved_money = float(input())
    money += saved_money
    if money >= vacation_money:
        money = 0
        print(f'Going to {destination}!')
        destination = input()
        if destination != "End":
            vacation_money = float(input())


