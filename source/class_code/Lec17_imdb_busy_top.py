imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

counts = dict()
for line in open(imdb_file, encoding = "utf-8"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        print('Adding', counts[name])
        counts[name].add(words[1].strip().title())
        print('After', counts[name])
    else:
        counts[name] = set([words[1].strip().title()])
        print('Added', name, counts[name])
print(counts)
    
actors = dict()
for actor in counts:
    movies_ct = len(counts[actor])
    print(actor, counts[actor])
    if movies_ct not in actors:
        actors[movies_ct] = list()
    actors[movies_ct].append(actor)
print(actors)