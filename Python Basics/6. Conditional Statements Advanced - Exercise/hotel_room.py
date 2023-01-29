month = input()
number_of_nights = int(input())

total_price_studio = 0
total_price_apartment = 0


if month == 'May' or month == 'October':
    if 7 < number_of_nights <= 14:
        total_price_studio = number_of_nights * 50 * 0.95
        total_price_apartment = number_of_nights * 65
    elif number_of_nights > 14:
        total_price_studio = number_of_nights * 50 * 0.70
        total_price_apartment = number_of_nights * 65 * 0.90
    else:
        total_price_studio = number_of_nights * 50
        total_price_apartment = number_of_nights * 65

elif month == 'June' or month == 'September':
    if number_of_nights > 14:
        total_price_studio = number_of_nights * 75.20 * 0.80
        total_price_apartment = number_of_nights * 68.70 * 0.90
    else:
        total_price_studio = number_of_nights * 75.20
        total_price_apartment = number_of_nights * 68.70

elif month == 'July' or month == 'August':
    if number_of_nights > 14:
        total_price_studio = number_of_nights * 76
        total_price_apartment = number_of_nights * 77 * 0.90
    else:
        total_price_studio = number_of_nights * 76
        total_price_apartment = number_of_nights * 77

print(f'Apartment: {total_price_apartment:.2f} lv.')
print(f'Studio: {total_price_studio:.2f} lv.')