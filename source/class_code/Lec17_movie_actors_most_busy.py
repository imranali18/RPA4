"""
Short program to demonstrate using a set as a value within a dictionary. 
For this example, we generate a movies dictionary where the keys are actor names
and the values are sets of movies with which they were associated. We then interrogate 
the dictionary to find out who is the busiest actor in unique movies.
"""


imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

"""
Generate the first dictionary by parsing the lines of the input file. Take
the actors name as the key and add the movie name into the set of movies
that the actor was associated with.
"""
movies = dict()
for line in open(imdb_file, encoding = "utf-8"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()

    if name in movies:
        movies[name].add(movie)
    else:
        movies[name] = set()
        movies[name].add(movie)
"""
Now go through the dictionary and see how many actors appeared in only one
unique movie and which actor was busiest based on associations with unique
movies.
"""
singlets = 0
most = 0
for name in movies:
    movie_ct = len(movies[name])
    if movie_ct == 1:
        singlets += 1
    if movie_ct > most:
        most = movie_ct
        person = name

print("{} appears most often: {} times".format(person, most))
print("{} people appear once".format(singlets))
