start_interval = input()
end_interval = input()
exception = input()
combination_counter = 0

for x in range(ord(start_interval), ord(end_interval) + 1):
    if x == ord(exception):
        continue
    for y in range(ord(start_interval), ord(end_interval) + 1):
        if y == ord(exception):
            continue
        for z in range(ord(start_interval), ord(end_interval) + 1):
            if z == ord(exception):
                continue
            combination_counter += 1
            print(f"{chr(x)}{chr(y)}{chr(z)}", end=" ")

print(combination_counter)


