number_of_dancers = int(input())
points = float(input())
season = input()
location = (input())

money_reward = 0

if location == "Bulgaria":
    money_reward = number_of_dancers * points
    if season == "summer":
        money_reward *= 0.95
    elif season == "winter":
        money_reward *= 0.92
elif location == "Abroad":
    money_reward = (number_of_dancers * points) * 1.50
    if season == "summer":
        money_reward *= 0.90
    elif season == "winter":
        money_reward *= 0.85

money_for_charity = money_reward * 0.75
money_reward *= 0.25
money_per_participant = money_reward / number_of_dancers

print(f'Charity - {money_for_charity:.2f}')
print(f'Money per dancer - {money_per_participant:.2f}')
