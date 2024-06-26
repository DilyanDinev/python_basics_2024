capacity = int(input())

income = 0
the_cinema_is_full = False
command = input()
while command != "Movie time!":
    number_of_people = int(command)
    if (capacity - number_of_people) >= 0:
        capacity -= number_of_people
        income += number_of_people * 5
        if number_of_people % 3 == 0:
            income -= 5
    else:
        the_cinema_is_full = True
        break
    command = input()

if the_cinema_is_full:
    print("The cinema is full.")
    print(f"Cinema income - {income} lv.")
else:
    print(f"There are {capacity} seats left in the cinema.")
    print(f"Cinema income - {income} lv.")
