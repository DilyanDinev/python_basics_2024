budget = float(input())
number_of_series = int(input())

for series in range(number_of_series):
    name_of_series = input()
    price_per_series = float(input())
    if name_of_series == "Thrones":
        price_per_series *= 0.5
        budget -= price_per_series
    elif name_of_series == "Lucifer":
        price_per_series *= 0.6
        budget -= price_per_series
    elif name_of_series == "Protector":
        price_per_series *= 0.7
        budget -= price_per_series
    elif name_of_series == "TotalDrama":
        price_per_series *= 0.8
        budget -= price_per_series
    elif name_of_series == "Area":
        price_per_series *= 0.9
        budget -= price_per_series
    else:
        budget -= price_per_series

if budget >= 0:
    print(f"You bought all the series and left with {budget:.2f} lv.")
else:
    print(f"You need {abs(budget):.2f} lv. more to buy the series!")