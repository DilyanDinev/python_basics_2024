chicken = int(input())
fish = int(input())
vegetarian = int(input())

price_chicken = chicken * 10.35
price_fish = fish * 12.4
price_vegetarian = vegetarian * 8.15

menu_price = price_chicken + price_fish + price_vegetarian

desert = menu_price * 0.2

total_price = menu_price + desert + 2.5

print(total_price)