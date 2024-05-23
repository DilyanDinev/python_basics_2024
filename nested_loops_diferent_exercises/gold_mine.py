number_of_location = int(input())

for _ in range(number_of_location):
    expected_avg_gold_per_day = float(input())
    number_of_days = int(input())
    gold = 0
    for day in range(number_of_days):
        gold_per_day = float(input())
        gold += gold_per_day
    avg_gold_per_day = gold / number_of_days
    if avg_gold_per_day >= expected_avg_gold_per_day:
        print(f"Good job! Average gold per day: {avg_gold_per_day:.2f}.")
    else:
        print(f"You need {expected_avg_gold_per_day - avg_gold_per_day:.2f} gold.")

