"""
Short program to demonstrate converting from one dictionary to another. For this 
example, we start by generating a movies dictionary where the keys are actor names
and the values are sets of movies with which they were associated. We turn that
into a second dictionary of occurrence frequency where the keys are a number
and the values are a list of the actors that have appeared in that number of movies
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
Now cycle through the movies dictionary to get the data for a new dictionary. This
time, for every actor, we calculate how many movies they were associated with by
taking the length of the set indicated by movies[name]. This length becomes a 
key in the actors dictionary where everyone who is associated with length number of
movies is stored in a list.
"""
actors = dict()
for name in movies:
    movie_ct = len(movies[name])
    if movie_ct not in actors:
        actors[movie_ct] = []
        actors[movie_ct].append(name)
    else:
        actors[movie_ct].append(name)

"""
Sort the actors dictionary from highest (most number of movies) to lowest 
(least number of movies). Print out the top 25 actors by number of movies 
they are associated with.
"""
keys = sorted(actors, reverse=True)
i = 0
count = 0
while count < 25 and i < len(keys):
    print(keys[i], actors[keys[i]])
    count += len(actors[keys[i]])
    i += 1