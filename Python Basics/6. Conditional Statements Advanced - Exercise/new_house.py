flower = input()
number_of_flowers = int(input())
budget = int(input())

rose_price = 5
dahlia_price = 3.80
tulips_price = 2.80
narcissus_price = 3
gladiolus_price = 2.50

total_price = 0

if flower == "Roses":
    if number_of_flowers > 80:
        total_price = number_of_flowers * rose_price * 0.9
    else:
        total_price = number_of_flowers * rose_price
elif flower == "Dahlias":
    if number_of_flowers > 90:
        total_price = number_of_flowers * dahlia_price * 0.85
    else:
        total_price = number_of_flowers * dahlia_price
elif flower == "Tulips":
    if number_of_flowers > 80:
        total_price = number_of_flowers * tulips_price * 0.85
    else:
        total_price = number_of_flowers * tulips_price
elif flower == "Narcissus":
    if number_of_flowers < 120:
        total_price = number_of_flowers * narcissus_price * 1.15
    else:
        total_price = number_of_flowers * narcissus_price
elif flower == "Gladiolus":
    if number_of_flowers < 80:
        total_price = number_of_flowers * gladiolus_price * 1.2
    else:
        total_price = number_of_flowers * gladiolus_price

differance = abs(budget-total_price)

if budget >= total_price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower} and {differance:.2f} leva left.")
else:
    print(f'Not enough money, you need {differance:.2f} leva more.')
