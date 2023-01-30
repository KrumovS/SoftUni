name_of_movie = input()

student_ticket = 0
standard_ticket = 0
kid_ticket = 0
sits_taken = 0

type_of_ticket = ""

while name_of_movie != "Finish":
    total_sits = int(input())
    sits_taken = 0
    type_of_ticket = ""
    while total_sits > sits_taken:
        type_of_ticket = input()
        if type_of_ticket == "student":
            student_ticket += 1
        elif type_of_ticket == "standard":
            standard_ticket += 1
        elif type_of_ticket == "kid":
            kid_ticket += 1
        elif type_of_ticket == "End":
            break
        sits_taken += 1
    sits_taken_percentage = (sits_taken / total_sits) * 100
    print(f'{name_of_movie} - {sits_taken_percentage:.2f}% full.')

    name_of_movie = input()

total_ticket_sold = student_ticket + standard_ticket + kid_ticket
student_ticket_percentage = (student_ticket/total_ticket_sold) * 100
standard_ticket_percentage = (standard_ticket/total_ticket_sold) * 100
kid_ticket_percentage = (kid_ticket/total_ticket_sold) * 100

print(f"Total tickets: {total_ticket_sold}")
print(f"{student_ticket_percentage:.2f}% student tickets.")
print(f"{standard_ticket_percentage:.2f}% standard tickets.")
print(f"{kid_ticket_percentage:.2f}% kids tickets.")
