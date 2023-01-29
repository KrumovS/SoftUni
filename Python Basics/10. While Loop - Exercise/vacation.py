vacation_money = float(input())
total_money = float(input())

saved_money = total_money
can_go_to_vacation = False
days_past = 0
spend_counter = 0


while spend_counter < 5:
    type_of_action = input()
    amount_of_money = float(input())
    days_past += 1
    if type_of_action == "spend":
        saved_money -= amount_of_money
        spend_counter += 1
        if saved_money < 0:
            saved_money = 0
    elif type_of_action =="save":
        saved_money += amount_of_money
        spend_counter = 0

    if saved_money >= vacation_money:
        can_go_to_vacation = True
        break

if can_go_to_vacation:
    print(f'You saved the money for {days_past} days.')
else:
    print(f"You can't save the money.")
    print(f"{days_past}")