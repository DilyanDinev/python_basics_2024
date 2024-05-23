from math import ceil, inf

number_of_easter_breads = int(input())
needed_packets_sugar = 0
needed_packets_flour = 0
max_used_flour = -inf
max_used_sugar = -inf
for easter_bread in range(number_of_easter_breads):
    current_quantity_sugar = int(input())
    current_quantity_flour = int(input())

    needed_packets_sugar += current_quantity_sugar
    needed_packets_flour += current_quantity_flour

    if current_quantity_sugar > max_used_sugar:
        max_used_sugar = current_quantity_sugar
    if current_quantity_flour > max_used_flour:
        max_used_flour = current_quantity_flour

needed_packets_sugar /= 950
needed_packets_flour /= 750
print(f"Sugar: {ceil(needed_packets_sugar)}")
print(f"Flour: {ceil(needed_packets_flour)}")
print(f"Max used flour is {max_used_flour} grams, max used sugar is {max_used_sugar} grams.")
