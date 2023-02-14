amount_for_the_day = int(input())
earn_amount = 0

command = input()

target_is_reached = False

while command != "closed":

    if command == "haircut":
        type_of_haircut = input()
        if type_of_haircut == "mens":
            earn_amount += 15
        elif type_of_haircut == "ladies":
            earn_amount += 20
        elif type_of_haircut == "kids":
            earn_amount += 10
    elif command == "color":
        type_of_color = input()
        if type_of_color == "touch up":
            earn_amount += 20
        elif type_of_color == "full color":
            earn_amount += 30
    if earn_amount >= amount_for_the_day:
        target_is_reached = True
        break

    command = input()

if target_is_reached:
    print(f'You have reached your target for the day!')
    print(f'Earned money: {earn_amount}lv.')
else:
    differance = abs(amount_for_the_day - earn_amount)
    print(f'Target not reached! You need {differance}lv. more.')
    print(f'Earned money: {earn_amount}lv.')
