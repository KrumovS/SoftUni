import sys

max_number = -sys.maxsize
number = input()

while number != "Stop":
    if max_number < int(number):
        max_number = int(number)
    number = input()

print(max_number)