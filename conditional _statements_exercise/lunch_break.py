from math import ceil

name_of_movie = input()
time_of_episode = int(input())
time_for_break = int(input())

time_for_lunch = time_for_break / 8
relax_time = time_for_break / 4
time_left = time_for_break - time_for_lunch - relax_time
difference = abs(time_left - time_of_episode)
difference = ceil(difference)

if time_left >= time_of_episode:
    print(f"You have enough time to watch {name_of_movie} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_movie}, you need {difference} more minutes.")