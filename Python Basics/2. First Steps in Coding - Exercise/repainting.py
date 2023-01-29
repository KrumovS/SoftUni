sq_of_nylon = int(input())
liters_of_paint = int(input())
paint_thinner = int(input())
hours_for_competion = int(input())

price_of_nylon = 1.50
price_of_paint = 14.50
price_of_thinner = 5.00

total_amount_for_nylon = (sq_of_nylon + 2) * price_of_nylon
total_amount_for_paint = (liters_of_paint + (liters_of_paint * 0.10)) * price_of_paint
total_amount_for_thinner = paint_thinner * price_of_thinner

total_amount_for_materials = total_amount_for_paint + total_amount_for_nylon + total_amount_for_thinner + 0.40

handyman_hour_fee = total_amount_for_materials * 0.3

needed_amount = total_amount_for_materials + handyman_hour_fee * hours_for_competion

print(needed_amount)


