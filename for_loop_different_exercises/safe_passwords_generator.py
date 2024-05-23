a = int(input())
b = int(input())
max_number_passwords = int(input())
password_counter = 0
flag = False
for A in range(35, 55 + 1):
    for B in range(64, 96 + 1):
        for x in range(1, a + 1):
            for y in range(1, b + 1):
                password_counter += 1

                if password_counter > max_number_passwords:
                    flag = True
                    break
                print(f"{chr(A)}{chr(B)}{x}{y}{chr(B)}{chr(A)}|", end="")
                if x == a and y == b:
                    flag = True
                    break
                A += 1
                if A > 55:
                    A = 35
                B += 1
                if B > 96:
                    B = 64

            if flag:
                break
        if flag:
            break
    if flag:
        break


