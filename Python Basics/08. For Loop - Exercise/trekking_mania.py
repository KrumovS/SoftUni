number_of_groups = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

total_number_of_people = 0

for i in range(number_of_groups):
    number_of_people = int(input())
    if number_of_people <= 5:
        p1 += number_of_people
    elif number_of_people <= 12:
        p2 += number_of_people
    elif number_of_people <= 25:
        p3 += number_of_people
    elif number_of_people <= 40:
        p4 += number_of_people
    elif number_of_people > 40:
        p5 += number_of_people
    total_number_of_people += number_of_people

musala_climbers = p1 / total_number_of_people * 100
monblan_climbers = p2 / total_number_of_people * 100
kili_climbers = p3 / total_number_of_people * 100
k2_climbers = p4 / total_number_of_people * 100
everest_climbers = p5 / total_number_of_people * 100

print(f'{musala_climbers:.2f}%')
print(f'{monblan_climbers:.2f}%')    
print(f'{kili_climbers:.2f}%')
print(f'{k2_climbers:.2f}%')
print(f'{everest_climbers:.2f}%')

