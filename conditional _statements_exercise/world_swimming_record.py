from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
seconds_for_one_meter = float(input())

all_distance_in_seconds = seconds_for_one_meter * distance_in_meters
delay = floor(distance_in_meters / 15) * 12.5
total_time = all_distance_in_seconds + delay
difference = abs(record_in_seconds - total_time)
if total_time < record_in_seconds:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference:.2f} seconds slower.")


