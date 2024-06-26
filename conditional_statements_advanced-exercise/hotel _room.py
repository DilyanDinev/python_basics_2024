month = input()
night = int(input())
price_per_studio = 0
price_per_apartment = 0

if month == "May" or month == "October":
    price_per_studio = 50
    price_per_apartment = 65
    if 7 < night <= 14:
        price_per_studio *= 0.95
    elif 14 < night:
        price_per_studio *= 0.7
        price_per_apartment *= 0.9

elif month == "June" or month == "September":
    price_per_studio = 75.2
    price_per_apartment = 68.7
    if 14 < night:
        price_per_studio *= 0.8
        price_per_apartment *= 0.9

elif month == "July" or month == "August":
    price_per_studio = 76
    price_per_apartment = 77
    if 14 < night:
        price_per_apartment *= 0.9

total_price_per_apartment = price_per_apartment * night
total_price_per_studio = price_per_studio * night

print(f"Apartment: {total_price_per_apartment:.2f} lv.")
print(f"Studio: {total_price_per_studio:.2f} lv.")



