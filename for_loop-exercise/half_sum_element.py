from sys import maxsize

number = int(input())

max_number = - maxsize
total_sum = 0

for i in range(number):
    current_number = int(input())
    total_sum += current_number
    if current_number > max_number:
        max_number = current_number

if max_number == total_sum - max_number:
    print("Yes")
    print(f"Sum = {max_number}")

else:
    difference = abs(max_number - (total_sum - max_number))
    print("No")
    print(f"Diff = {difference}")
