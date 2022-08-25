training_fee = int(input())

sneaker_price = training_fee - (training_fee * 0.4)
clothes_price = sneaker_price - (sneaker_price * 0.2)
ball_price = clothes_price * 0.25
accessories_price = ball_price * 0.20

total_amount = sneaker_price + clothes_price + ball_price + accessories_price + training_fee

print(total_amount)
