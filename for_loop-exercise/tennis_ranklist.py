number_of_tournaments = int(input())
start_points = int(input())
total_points = start_points
won = 0
final = 0
semi_final = 0

for _ in range(number_of_tournaments):
    stage_of_tournament = input()
    if stage_of_tournament == "W":
        total_points += 2000
        won += 1
    elif stage_of_tournament == "F":
        total_points += 1200
        final += 1
    elif stage_of_tournament == "SF":
        total_points += 720
        semi_final += 1

average_points = (total_points - start_points) / number_of_tournaments
percent_won = (won / number_of_tournaments) * 100

print(f"Final points: {total_points}")
print(f"Average points: {int(average_points)}")
print(f"{percent_won:.2f}%")