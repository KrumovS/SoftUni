from math import floor

world_record = float(input())
distance = float(input())
meters_per_second = float(input())

delay = floor(distance // 15) * 12.5
ivancho_time = distance * meters_per_second + delay

differance = abs(world_record - ivancho_time)

if world_record > ivancho_time:
    print(f'Yes, he succeeded! The new world record is {ivancho_time:.2f} seconds.')

else:
    print(f'No, he failed! He was {differance:.2f} seconds slower.')


