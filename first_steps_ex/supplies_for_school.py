number_of_pens = int(input())
number_of_markers = int(input())
liters_of_preparation = int(input())
percent_discount = int(input())

price_per_pens = number_of_pens * 5.8
price_per_markers = number_of_markers * 7.2
price_preparation = liters_of_preparation * 1.2

needed_money = price_per_pens + price_per_markers + price_preparation
discount = needed_money * percent_discount / 100
total_price = needed_money - discount
print(total_price)



