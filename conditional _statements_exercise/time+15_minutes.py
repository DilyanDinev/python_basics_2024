hour = int(input())
minuets = int(input())

minuets += 15
hour += minuets // 60
minuets %= 60

if hour > 23:
    hour = 0

print(f"{hour}:{minuets:02d}")