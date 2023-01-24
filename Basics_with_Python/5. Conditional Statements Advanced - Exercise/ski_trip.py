days = int(input())
type_of_room = input()
feedback = input()

nights = days - 1
price = 0

if type_of_room == "room for one person":
    price = nights * 18
elif type_of_room == "apartment":
    if days < 10:
        price = nights * 25 * 0.70
    elif days <= 15:
        price = nights * 25 * 0.65
    else:
        price = nights * 25 * 0.5
elif type_of_room == "president apartment":
    if days < 10:
        price = nights * 35 * 0.90
    elif days <= 15:
        price = nights * 35 * 0.85
    else:
        price = nights * 35 * 0.80

if feedback == "positive":
    price *= 1.25
elif feedback == "negative":
    price *= 0.90

print(f'{price:.2f}')
