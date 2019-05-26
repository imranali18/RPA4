imdb_file = input("Enter the name of the IMDB file ==> ").strip()
movies = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    movie = words[1].strip()
    if movie in movies:
        movies[movie].add(name)
    else:
        movies[movie] = set()
        movies[movie].add(name)

most = 0
counter = 0
for movie in movies:
    if len(movies[movie]) == 1:
        counter += 1
    if len(movies[movie]) > most:
        most = len(movies[movie])
        title = movie

print(most)
print(title)
print(counter)