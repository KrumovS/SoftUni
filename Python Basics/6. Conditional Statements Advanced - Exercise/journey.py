budget = float(input())
season = input()

destination = ''
accommodation = ''
vacation = 0

if budget <= 100:
    if season == "summer":
        vacation = budget * 0.3
    else:
        vacation = budget * 0.7

    destination = "Bulgaria"

elif budget <= 1000:
    if season == "summer":
        vacation = budget * 0.4
    else:
        vacation = budget * 0.8

    destination = "Balkans"
else:
    vacation = budget * 0.9
    destination = "Europe"
if season == "summer" and destination != "Europe":
    accommodation = "Camp"
elif season == "winter" or destination == "Europe":
    accommodation = "Hotel"

print(f'Somewhere in {destination} ')
print(f'{accommodation} - {vacation:.2f}')
