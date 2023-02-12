number_of_students = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
total_grade = 0

for i in range (number_of_students):
    grade = float(input())
    total_grade += grade

    if grade >= 5.00:
        p1 += 1
    elif grade >= 4.00:
        p2 += 1
    elif grade >= 3.00:
        p3 += 1
    else:
        p4 += 1

p1 = (p1 / number_of_students) * 100
p2 = (p2 / number_of_students) * 100
p3 = (p3 / number_of_students) * 100
p4 = (p4 / number_of_students) * 100

average_grade = total_grade / number_of_students

print(f'Top students: {p1:.2f}%')
print(f'Between 4.00 and 4.99: {p2:.2f}%')
print(f'Between 3.00 and 3.99: {p3:.2f}%')
print(f'Fail: {p4:.2f}%')
print(f'Average: {average_grade:.2f}')

