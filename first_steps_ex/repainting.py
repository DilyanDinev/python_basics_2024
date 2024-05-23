nylon = float(input())
paint = float(input())
razr = int(input())
hours = int(input())

price_nylon = (nylon + 2) * 1.5
price_paint = paint * 14.5 + (paint * 14.5) * 0.1
price_razr = razr * 5
expenses = price_nylon + price_paint + price_razr + 0.4
price_per_hour_work = expenses * 30 / 100
total_price = expenses + hours * price_per_hour_work

print(total_price)

#nylon = int(input())
#paint = int(input())
#razr = int(input())
#hours_work = int(input())

#price_nylon = (nylon + 2) * 1.5
#price_paint = 14.5 * paint * 1.1
#price_razr = razr * 5
#bag = 0.4

#materials_price = price_nylon + price_paint + price_razr + bag
#price_per_hour_work = materials_price * 0.3 * hours_work
#total_price = materials_price + price_per_hour_work
#print(total_price)