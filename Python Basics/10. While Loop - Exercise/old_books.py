searched_book = input()
found_book = input()

condition = False
counter = 0


while found_book != "No More Books":
    if searched_book == found_book:
        condition = True
        break

    found_book = input()
    counter += 1

if condition:
    print(f"You checked {counter} books and found it.")
else:
    print(f'The book you search is not here!')
    print(f'You checked {counter} books.')