hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

total_minutes_of_exam = hour_of_exam * 60 + minutes_of_exam
total_minutes_of_arrival = hour_of_arrival * 60 + minutes_of_arrival

differance = total_minutes_of_exam - total_minutes_of_arrival

if 0 <= differance <= 30:
    condition = "On time"
elif differance < 0:
    condition = "Late"
elif differance > 30:
    condition = "Early"

differance = abs(differance)
hours = differance // 60
minutes = differance % 60

if condition == "On time" and differance == 0:
    print(f'{condition}')
elif condition == "On time" and differance != 0:
    print(f'{condition}')
    print(f'{differance} minutes before the start')
elif condition == "Late":
    print(f'{condition}')
    if hours != 0:
        print(f'{hours}:{minutes:02d} hours after the start')
    else:
        print(f'{minutes} minutes after the start')
elif condition == "Early":
    print(f'{condition}')
    if hours != 0:
        print(f'{hours}:{minutes:02d} hours before the start')
    else:
        print(f'{minutes} minutes before the start')
