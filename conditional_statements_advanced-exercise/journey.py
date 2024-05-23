budget = float(input())
season = input()

holiday_country = ""
holiday_place = ""
price = 0

if budget <= 100:
    holiday_country = "Bulgaria"
    if season == "summer":
        holiday_place = "Camp"
        price = budget * 0.3
    elif season == "winter":
        holiday_place = "Hotel"
        price = budget * 0.7

elif 1000 >= budget:
    holiday_country = "Balkans"
    if season == "summer":
        holiday_place = "Camp"
        price = budget * 0.4
    elif season == "winter":
        holiday_place = "Hotel"
        price = budget * 0.8

elif 1000 < budget:
    holiday_country = "Europe"
    holiday_place = "Hotel"
    price = budget * 0.9

print(f"Somewhere in {holiday_country}")
print(f"{holiday_place} - {price:.2f}")