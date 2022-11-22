movie_name = []
movie_number = input("How many movies do you want to add?: ")
movie_number = int(movie_number)
for i in range(movie_number):
    name = input("Enter the name of a movie: ")
    movie_name.append(name)
print(movie_name)