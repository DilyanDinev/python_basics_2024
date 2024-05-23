from math import inf

movie_name = input()
winner_name = ""
movie_counter = 0
max_value = -inf
while movie_name != "STOP":
    movie_counter += 1
    if movie_counter == 7:
        print("The limit is reached.")
        break

    symbol_sym = 0

    for letter in movie_name:
        ascii_value = ord(letter)
        if "a" <= letter <= "z":
            symbol_sym += ascii_value - (len(movie_name) * 2)
        elif "A" <= letter <= "Z":
            symbol_sym += ascii_value - len(movie_name)
        else:
            symbol_sym += ascii_value

    if symbol_sym > max_value:
        max_value = symbol_sym
        winner_name = movie_name
    movie_name = input()
print(f"The best movie for you is {winner_name} with {max_value} ASCII sum.")

