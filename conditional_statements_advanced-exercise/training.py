minutes = int(input())
seconds = int(input())
length_in_meters = float(input())
hundred_meters_seconds = int(input())

time_in_seconds = minutes * 60 + seconds

delay_in_meters = length_in_meters / 120
delay_in_seconds = delay_in_meters * 2.5
time = hundred_meters_seconds * length_in_meters / 60
total_time = time - 25


difference = abs(time_in_seconds - total_time)
if total_time <= minutes:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")