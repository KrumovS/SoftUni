import math

number_of_tournaments = int(input())
starting_points = int(input())

p1 = 0
points_this_season = 0

for i in range (number_of_tournaments):
    result = input()
    if result == "W":
        points_this_season += 2000
        p1 += 1
    elif result == "F":
        points_this_season += 1200
    elif result == "SF":
        points_this_season += 720

starting_points += points_this_season
average_points = points_this_season / number_of_tournaments
win_percentage = (p1 / number_of_tournaments) * 100

print(f'Final points: {starting_points}')
print(f'Average points: {math.floor(average_points)}')
print(f'{win_percentage:.2f}%')




