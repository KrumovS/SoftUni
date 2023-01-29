name = input()

average_grade = 0

p1 = 0
p2 = 1

while True:
    grade = float(input())

    if grade < 4:
        p1 += 1
        if p1 == 2:
            print(f'{name} has been excluded at {p2} grade')
            break
    else:
        p2 += 1
        average_grade += grade
        if p2 > 12:
            average_grade /= 12
            print(f'{name} graduated. Average grade: {average_grade:.2f}')
            break
