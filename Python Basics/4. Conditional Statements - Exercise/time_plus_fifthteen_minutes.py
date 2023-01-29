hour = int(input())
minutes = int(input()) + 15

hour += minutes // 60
minutes %= 60

if hour == 24:
    hour = 0

if minutes <=9:
    print(f'{hour}:0{minutes}')

else:
    print(f'{hour}:{minutes}')
