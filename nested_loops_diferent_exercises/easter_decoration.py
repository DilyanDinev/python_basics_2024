number_of_customer = int(input())
total_sum = 0

for easter in range(number_of_customer):
    number_of_products = 0
    current_sum = 0
    command = input()
    while command != "Finish":
        number_of_products += 1
        if command == "basket":
            current_sum += 1.5
        elif command == "wreath":
            current_sum += 3.8
        elif command == "chocolate bunny":
            current_sum += 7
        command = input()

    if number_of_products % 2 == 0:
        current_sum *= 0.8
    total_sum += current_sum
    print(f"You purchased {number_of_products} items for {current_sum:.2f} leva.")

avg_sum = total_sum / number_of_customer
print(f"Average bill per client is: {avg_sum:.2f} leva.")