projection = input()
lines = int(input())
columns = int(input())
price = 0

if projection == "Premiere":
    price = lines * columns * 12

elif projection == "Normal":
    price = lines * columns * 7.5

elif projection == "Discount":
    price = lines * columns * 5

print(f"{price:.2f}")