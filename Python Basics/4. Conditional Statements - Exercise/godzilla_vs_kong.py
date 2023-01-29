film_budget = float(input())
number_of_statists = int(input())
price_of_clothes = float(input())

decor_price = film_budget * 0.1

if number_of_statists > 150:
    price_of_clothes *= 0.9

needed_amount = number_of_statists * price_of_clothes + decor_price
differance = abs(film_budget - needed_amount)

if film_budget < needed_amount:
    print(f'Not enough money!')
    print(f'Wingard needs {differance:.2f} leva more.')

else:
    print(f'Action!')
    print(f'Wingard starts filming with {differance:.2f} leva left.')
