budget = float(input())

not_enough_money = False
command = input()
while command != "ACTION":
    name_of_actor = command

    if len(name_of_actor) <= 15:
        salary = float(input())
        if salary > budget:
            difference = abs(budget - salary)
            not_enough_money = True
            break
        else:
            budget -= salary
    else:
        budget -= budget * 0.2
    command = input()

if not_enough_money:
    print(f"We need {difference:.2f} leva for our actors.")
else:
    print(f"We are left with {budget:.2f} leva.")