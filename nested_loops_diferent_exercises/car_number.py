start_interval = int(input())
end_interval = int(input())

for number_1 in range(start_interval, end_interval + 1):
    for number_2 in range(start_interval, end_interval + 1):
        for number_3 in range(start_interval, end_interval + 1):
            for number_4 in range(start_interval, end_interval + 1):
                different = True
                if number_1 % 2 == 0 and number_4 % 2 == 0 or number_1 % 2 != 0 and number_4 % 2 != 0:
                    different = False
                if number_4 < number_1 and (number_2 + number_3) % 2 == 0 and different:
                    print(f"{number_1}{number_2}{number_3}{number_4}", end=" ")