large = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = large * width * height
needed_liters_in_centimeters = volume * (1 - percent / 100)
needed_liters = needed_liters_in_centimeters / 1000

print(needed_liters)

