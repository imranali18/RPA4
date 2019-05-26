imdb_file = input("Enter the name of the IMDB file ==> ").strip()
counts = dict()
for line in open(imdb_file, encoding="utf-8"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
        
names = sorted(counts)
limit = min(100, len(names))
for index in range(limit):
    name = names[index]
    print("{} appeared in {} movies".format(name, counts[name]))
