days = int(input())
type_of_room = input()
evaluation = input()
nights = days - 1
price = 0

if type_of_room == "room for one person":
    price = 18

elif type_of_room == "apartment":
    price = 25
    if nights < 10:
        price *= 0.7
    elif 10 <= nights <= 15:
        price *= 0.65
    elif nights > 15:
        price *= 0.5

elif type_of_room == "president apartment":
    price = 35
    if nights < 10:
        price *= 0.9
    elif 10 <= nights <= 15:
        price *= 0.85
    elif nights > 15:
        price *= 0.8

total_price = price * nights

if evaluation == "positive":
    total_price *= 1.25
elif evaluation == "negative":
    total_price *= 0.9

print(f"{total_price:.2f}")

