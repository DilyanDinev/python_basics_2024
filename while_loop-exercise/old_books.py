name_of_book = input()

chek_counter = 0
is_book_found = False
current_book = input()

while current_book != "No More Books":
    if current_book == name_of_book:
        is_book_found = True
        break

    chek_counter += 1
    current_book = input()

if is_book_found:
    print(f"You checked {chek_counter} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {chek_counter} books.")
