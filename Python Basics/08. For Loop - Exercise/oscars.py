name_of_actor = input()
starting_points = float(input())
number_of_jury = int(input())

for i in range(number_of_jury):
    name_of_the_jury = input()
    points = float(input())
    points_given = len(name_of_the_jury) * points / 2

    starting_points += points_given
    if starting_points >= 1250.5:
        break

if starting_points >= 1250.5:
    print(f'Congratulations, {name_of_actor} got a nominee for leading role with {starting_points:.1f}!')
else:
    diff = abs(starting_points - 1250.5)
    print(f'Sorry, {name_of_actor} you need {diff:.1f} more!')
