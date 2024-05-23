number = int(input())

total_number = 0

for numbers in range(number):
    first_number = int(input())
    second_number = int(input())
    total_number += first_number + second_number

value = total_number / number
if value == first_number + second_number:
    print(f"Yes, value={int(value)}")
else:
    difference = abs(number - value)
    print(f"No, maxdiff={int(difference)}")
