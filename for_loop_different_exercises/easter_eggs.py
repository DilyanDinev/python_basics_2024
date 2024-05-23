from math import inf

number_of_painted_eggs = int(input())

max_number = -inf
red_color = 0
orange_color = 0
blue_color = 0
green_color = 0

for _ in range(number_of_painted_eggs):
    current_color_of_egg = input()

    if current_color_of_egg == "red":
        red_color += 1
        if red_color > max_number:
            max_number = red_color
            max_color = "red"
    elif current_color_of_egg == "orange":
        orange_color += 1
        if orange_color > max_number:
            max_number = orange_color
            max_color = "orange"
    elif current_color_of_egg == "blue":
        blue_color += 1
        if blue_color > max_number:
            max_number = blue_color
            max_color = "blue"
    elif current_color_of_egg == "green":
        green_color += 1
        if green_color > max_number:
            max_number = green_color
            max_color = "green"

print(f"Red eggs: {red_color}")
print(f"Orange eggs: {orange_color}")
print(f"Blue eggs: {blue_color}")
print(f"Green eggs: {green_color}")
print(f"Max eggs: {max_number} -> {max_color}")