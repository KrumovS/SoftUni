packs_of_pens = int(input())
packs_of_markers = int(input())
detergent = int(input())
discount = float(input())

price_of_pack_of_pens = 5.80
price_of_pack_of_markers = 7.20
price_of_detergent = 1.20

total_price_of_pens = packs_of_pens * price_of_pack_of_pens
total_price_of_markers = packs_of_markers * price_of_pack_of_markers
total_price_of_detergent = detergent * price_of_detergent

total_amount = total_price_of_pens + total_price_of_markers + total_price_of_detergent

discount = total_amount * (discount / 100)

total_amount = total_amount - discount

print(total_amount)
