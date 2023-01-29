import sys

min_number = sys.maxsize
number = input()

while number != "Stop":
    if min_number > int(number):
        min_number = int(number)
    number = input()

print(min_number)