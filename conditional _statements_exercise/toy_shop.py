needed_money = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
total_sum = number_of_puzzles * 2.6 \
            + number_of_dolls * 3 \
            + number_of_bears * 4.1 \
            + number_of_minions * 8.2 \
            + number_of_trucks * 2
total_number_of_toys = number_of_puzzles \
                       + number_of_dolls \
                       + number_of_bears \
                       + number_of_minions \
                       + number_of_trucks
if total_number_of_toys >= 50:
    total_sum *= 0.75
total_sum *= 0.9
difference = abs(needed_money - total_sum)
if total_sum >= needed_money:
    print(f"Yes! {difference:.2f} lv left.")
else:
    print(f"Not enough money! {difference:.2f} lv needed.")
