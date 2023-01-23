budget = int(input())
season = input()
number_of_fisherman = int(input())

if season == "Spring":
    ship_price = 3000
    if number_of_fisherman <= 6:
        ship_price *= 0.9
    elif  7 <= number_of_fisherman <= 11:
        ship_price *= 0.85
    else:
        ship_price *= 0.75
elif season == "Summer" or season == "Autumn":
    ship_price = 4200
    if number_of_fisherman <= 6:
        ship_price *= 0.9
    elif 7 <= number_of_fisherman <= 11:
        ship_price *= 0.85
    else:
        ship_price *= 0.75
elif season == "Winter":
    ship_price = 2600
    if number_of_fisherman <= 6:
        ship_price *= 0.9
    elif 7 <= number_of_fisherman <= 11:
        ship_price *= 0.85
    else:
        ship_price *= 0.75
if not season == "Autumn" and number_of_fisherman % 2 == 0:
    ship_price *= 0.95

differance = abs(budget - ship_price)

if budget >= ship_price:
    print(f"Yes! You have {differance:.2f} leva left.")
else:
    print(f"Not enough money! You need {differance:.2f} leva.")