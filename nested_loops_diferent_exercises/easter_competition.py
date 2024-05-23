number_of_easter_bread = int(input())
winner_name = ""
win_points = - 100

for easter_bread in range(number_of_easter_bread):
    baker_name = input()
    points = 0
    command = input()
    while command != "Stop":
        current_points = int(command)
        points += current_points
        command = input()
    print(f"{baker_name} has {points} points.")
    if points > win_points:
        win_points = points
        winner_name = baker_name
        print(f"{baker_name} is the new number 1!")
print(f"{winner_name} won competition with {win_points} points!")