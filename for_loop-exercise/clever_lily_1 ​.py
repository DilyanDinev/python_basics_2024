ages = int(input())
price_per_laundry = float(input())
price_per_toy = int(input())

current_birthday_money = 0
total_toy = 0
total_money = 0

for birthday in range(1, ages + 1):
    if birthday % 2 == 0:
        current_birthday_money += 10
        total_money += current_birthday_money - 1
    else:
        total_toy += 1
total_money += total_toy * price_per_toy

difference = abs(price_per_laundry - total_money)

if total_money >= price_per_laundry:
    print(f"Yes! {difference:.2f}")
else:
    print(f"No! {difference:.2f}")