from math import inf

number_of_movies = int(input())
max_movie_rating = ""
min_movie_rating = ""
max_rating = 0
min_rating = inf
average_rating = 0
for movies in range(number_of_movies):
    name_of_movie = input()
    rating_of_movie = float(input())
    average_rating += rating_of_movie
    if rating_of_movie > max_rating:
        max_rating = rating_of_movie
        max_movie_rating = name_of_movie
    if rating_of_movie < min_rating:
        min_rating = rating_of_movie
        min_movie_rating = name_of_movie

average_rating /= number_of_movies
print(f"{max_movie_rating} is with highest rating: {max_rating:.1f}")
print(f"{min_movie_rating} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")

