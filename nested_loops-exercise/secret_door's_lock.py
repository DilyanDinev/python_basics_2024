hundreds = int(input())
dozens = int(input())
units = int(input())
flag = False
for number_1 in range(1, hundreds + 1):
    for number_2 in range(1, dozens + 1):
        for number_3 in range(1, units + 1):
            if number_2 == 2 or number_2 == 3 or number_2 == 5 or number_2 == 7:
                flag = True
                if flag and number_1 % 2 == 0 and number_3 % 2 == 0:
                    print(f"{number_1} {number_2} {number_3}")
