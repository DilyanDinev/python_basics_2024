number_of_men = int(input())
number_of_women = int(input())
max_number_of_table = int(input())

for men in range(1, number_of_men + 1):
    for women in range(1, number_of_women + 1):
        if max_number_of_table == 0:
            break
        print(f"({men} <-> {women})", end=" ")
        max_number_of_table -= 1

