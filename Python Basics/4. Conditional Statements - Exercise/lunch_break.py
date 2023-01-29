from math import ceil

name_of_tv_series = str(input())
length_of_the_episode = int(input())
length_of_the_break = int(input())

length_of_lunch = length_of_the_break * (1 / 8)
length_of_rest = length_of_the_break * (1 / 4)

time_left = length_of_the_break - length_of_lunch - length_of_rest


if length_of_the_episode <= time_left:
    time_left = ceil(abs(time_left - length_of_the_episode))
    print(f"You have enough time to watch {name_of_tv_series} and left with {time_left} minutes free time.")

else:
    time_left = ceil(abs(time_left - length_of_the_episode))
    print(f"You don't have enough time to watch {name_of_tv_series}, you need {time_left} more minutes.")


