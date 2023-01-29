screening_type = input()
rows = int(input())
columns = int(input())

premiere = 12.00
normal = 7.50
discount = 5.00
cinema_income = 0

cinema_hall = rows * columns

if screening_type == "Premiere":
    cinema_income = cinema_hall * premiere
elif screening_type == "Normal":
    cinema_income = cinema_hall * normal
elif screening_type == "Discount":
    cinema_income = cinema_hall * discount

print(f'{cinema_income:.2f} leva')
