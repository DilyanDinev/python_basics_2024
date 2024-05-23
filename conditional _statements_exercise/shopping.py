budget = float(input())
number_video_cards = int(input())
number_processor = int(input())
number_ram_memory = int(input())

video_card_price = number_video_cards * 250
processor_price = video_card_price * 0.35 * number_processor
ram_memory_price = video_card_price * 0.1 * number_ram_memory
total_price = video_card_price + processor_price + ram_memory_price

if number_video_cards > number_processor:
    total_price *= 0.85
difference = abs(budget - total_price)
if total_price <= budget:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
