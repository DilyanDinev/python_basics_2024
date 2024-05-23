last_sector = input()
number_of_rows_first_sector = int(input())
number_of_seats_of_odd_row = int(input())
total_seats = 0
for sector in range(ord("A"), ord(last_sector) + 1):
    for row in range(1, number_of_rows_first_sector + 1):
        current_seats = number_of_seats_of_odd_row
        if row % 2 == 0:
            for seat in range(97, 97 + number_of_seats_of_odd_row + 2):
                print(f"{chr(sector)}{row}{chr(seat)}")
                total_seats += 1
        else:
            for seat in range(97, 97 + number_of_seats_of_odd_row):
                print(f"{chr(sector)}{row}{chr(seat)}")
                total_seats += 1
    number_of_rows_first_sector += 1
print(total_seats)

