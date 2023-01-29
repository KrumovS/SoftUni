length = int(input())
width = int(input())

cake_size = length * width


while cake_size > 0:
    cake_piece = input()
    if cake_piece == "STOP":
        break
    else:
        cake_size -= int(cake_piece)

if cake_size >= 0:
    print(f'{cake_size} pieces are left.')
else:
    print(f'No more cake left! You need {abs(cake_size)} pieces more.')