length = int(input())
width = int(input())
height = int(input())
fill_rate = float(input())

volume = length * width * height
volume_in_liters = volume * 0.001
fill_rate = fill_rate / 100

volume_in_liters = volume_in_liters * (1 - fill_rate)

print(volume_in_liters)