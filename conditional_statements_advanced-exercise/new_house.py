type_of_flower = input()
number_of_flower = int(input())
budget = int(input())

price = 0

if type_of_flower == "Roses":
    price = 5
    if number_of_flower > 80:
        price *= 0.9

elif type_of_flower == "Dahlias":
    price = 3.8
    if number_of_flower > 90:
        price *= 0.85

elif type_of_flower == "Tulips":
    price = 2.8
    if number_of_flower > 80:
        price *= 0.85


elif type_of_flower == "Narcissus":
    price = 3
    if number_of_flower < 120:
        price *= 1.15

elif type_of_flower == "Gladiolus":
    price = 2.5
    if number_of_flower < 80:
        price *= 1.2

needed_sum = price * number_of_flower
difference = abs(budget - needed_sum)

if budget >= needed_sum:
    print(f"Hey, you have a great garden with {number_of_flower} {type_of_flower} and {difference:.2f} leva left.")

else:
    print(f"Not enough money, you need {difference:.2f} leva more.")


