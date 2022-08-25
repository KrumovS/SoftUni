chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

price_of_chicken_menu = 10.35
price_of_fish_menu = 12.40
price_of_veggie_menu = 8.15

total_amount_of_chicken_menu = chicken_menu * price_of_chicken_menu
total_amount_of_fish_menu = fish_menu * price_of_fish_menu
total_amount_of_veggie_menu = veggie_menu * price_of_veggie_menu

total_amount_of_food = total_amount_of_fish_menu + total_amount_of_chicken_menu + total_amount_of_veggie_menu

price_of_desert = total_amount_of_food * 0.2

total_amount_of_food = total_amount_of_food + price_of_desert + 2.50

print(total_amount_of_food)
