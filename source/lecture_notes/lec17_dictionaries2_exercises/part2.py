imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

movies = dict()

for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    actor = words[0].strip()
    movie = words[1].strip()
    if movie in movies:
        movies[movie].add(actor)
    else:
        movies[movie] = set([actor])

most_value = -1
most_names = []
only_one = 0
for m in movies:
    if len(movies[m]) > most_value:
        most_value = len(movies[m])
        most_names = [ m ]
    elif len(movies[m]) == most_value:
        most_names.append(m)
    if len(movies[m]) == 1:
        only_one += 1

print(most_value)
print(most_names[0])
print(only_one)

