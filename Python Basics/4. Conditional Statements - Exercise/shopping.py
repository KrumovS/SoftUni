petar_budget = float(input())
graphic_cards = int(input())
processors = int(input())
ram = int(input())

graphic_card_price = 250

graphic_card_price = graphic_cards * graphic_card_price
processor_price = graphic_card_price * 0.35 * processors
ram_price = graphic_card_price * 0.1 * ram

total_price = graphic_card_price + processor_price + ram_price

if graphic_cards > processors:
    total_price *= 0.85

differance = abs(petar_budget - total_price)

if petar_budget >= total_price:
    print(f"You have {differance:.2f} leva left!")

else:
    print(f"Not enough money! You need {differance:.2f} leva more!")



