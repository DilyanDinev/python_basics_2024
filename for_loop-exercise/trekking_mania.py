number_of_groups = int(input())

musala_climbers = 0
montblanc_climbers = 0
kilimanjaro_climbers = 0
k2_climbers = 0
everest_climbers = 0

for current_group in range(number_of_groups):
    current_number = int(input())
    if current_number <= 5:
        musala_climbers += current_number
    elif current_number <= 12:
        montblanc_climbers += current_number
    elif current_number <= 25:
        kilimanjaro_climbers += current_number
    elif current_number <= 40:
        k2_climbers += current_number
    elif current_number >= 41:
        everest_climbers += current_number

total_climbers = musala_climbers \
                 + montblanc_climbers \
                 + kilimanjaro_climbers \
                 + k2_climbers \
                 + everest_climbers
percent_musala_climbers = musala_climbers / total_climbers * 100
percent_montblanc_climbers = montblanc_climbers / total_climbers * 100
percent_kilimanjaro_climbers = kilimanjaro_climbers / total_climbers * 100
percent_k2_climbers = k2_climbers / total_climbers * 100
percent_everest_climbers = everest_climbers / total_climbers * 100

print(f"{percent_musala_climbers:.2f}%")
print(f"{percent_montblanc_climbers:.2f}%")
print(f"{percent_kilimanjaro_climbers:.2f}%")
print(f"{percent_k2_climbers:.2f}%")
print(f"{percent_everest_climbers:.2f}%")
