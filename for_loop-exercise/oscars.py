name_of_actor = input()
points_academy = float(input())
number_of_jury = int(input())
total_points = points_academy

for current_points in range(number_of_jury):
    name_of_jury = input()
    points_of_one_person = float(input())
    points = len(name_of_jury) * points_of_one_person / 2
    total_points += points
    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {name_of_actor} got a nominee for leading role with {total_points:.1f}!")
else:
    needed_point = 1250.5 - total_points
    print(f"Sorry, {name_of_actor} you need {needed_point:.1f} more!")






