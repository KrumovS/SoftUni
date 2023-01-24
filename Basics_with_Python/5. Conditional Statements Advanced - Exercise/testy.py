hour_of_exam = int(input())
minutes_of_exam = int(input())
hour_of_arrival = int(input())
minutes_of_arrival = int(input())

total_minutes_of_exam = hour_of_exam * 60 + minutes_of_exam
total_minutes_of_arrival = hour_of_arrival * 60 + minutes_of_arrival

differance = total_minutes_of_exam - total_minutes_of_arrival

print(differance)