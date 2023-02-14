tshirt_price = float(input())
amount_needed_for_reward = float(input())

shorts_price = tshirt_price * 0.75
socks_price = shorts_price * 0.20
shoe_price = (tshirt_price + shorts_price) * 2
discount = (100-15) / 100

total_price = (tshirt_price + shorts_price + socks_price + shoe_price) * discount
differance = abs(total_price - amount_needed_for_reward)

if total_price >= amount_needed_for_reward:
    print(f'Yes, he will earn the world-cup replica ball!')
    print(f'His sum is {total_price:.2f} lv.')
else:
    print(f'No, he will not earn the world-cup replica ball.')
    print(f'He needs {differance:.2f} lv. more.')