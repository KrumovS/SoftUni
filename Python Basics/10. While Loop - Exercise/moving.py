length = int(input())
width = int(input())
height = int(input())
number_of_boxes = input()

room_size = length * width * height

free_space = True

while number_of_boxes != "Done":
    room_size -= int(number_of_boxes)
    if room_size < 0:
        free_space = False
        break

    number_of_boxes = input()

if not free_space:
    print(f'No more free space! You need {abs(room_size)} Cubic meters more.')
else:
    print(f'{room_size} Cubic meters left.')
