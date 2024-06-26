budget = float(input())
total_price = 0
total_counter = 0
products_counter = 0
more_expensive = False
command = input()
while command != "Stop":
    name_of_product = command
    product_price = float(input())
    total_counter += 1
    products_counter += 1
    if products_counter == 3:
        product_price /= 2
        total_price += product_price
        products_counter = 0
    else:
        total_price += product_price
    if product_price > budget:
        more_expensive = True
        break
    else:
        budget -= product_price
    command = input()

if more_expensive:
    print("You don't have enough money!")
    print(f"You need {product_price - budget:.2f} leva!")
else:
    print(f"You bought {total_counter} products for {total_price:.2f} leva.")