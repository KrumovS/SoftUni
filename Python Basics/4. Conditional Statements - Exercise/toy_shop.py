trip = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

puzzle_price = 2.60
doll_price = 3
bear_price = 4.10
minion_price = 8.20
truck_price = 2

total_price_of_puzzles = number_of_puzzles * puzzle_price
total_price_of_dolls = number_of_dolls * doll_price
total_price_of_bears = number_of_bears * bear_price
total_price_of_minions = number_of_minions * minion_price
total_price_of_trucks = number_of_trucks * truck_price

toys_sold = number_of_puzzles + number_of_dolls + number_of_bears + number_of_minions + number_of_trucks
earned_amount = (total_price_of_puzzles + total_price_of_dolls + total_price_of_bears + total_price_of_minions + \
               total_price_of_trucks)

if toys_sold >= 50:
    earned_amount *= 0.75
    earned_amount *= 0.9

else:
    earned_amount *= 0.9

if trip <= earned_amount:
    money_left = abs(trip - earned_amount)
    print(f"Yes! {money_left:.2f} lv left.")

else:
    money_left = abs(trip - earned_amount)
    print(f"Not enough money! {money_left:.2f} lv needed.")








