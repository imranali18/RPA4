imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

counts = dict()
for line in open(imdb_file, encoding = "utf-8"):
    words = line.strip().split('|')
    name = words[0].strip()
    if name in counts:
        counts[name].add(words[1].strip().title())
    else:
        counts[name] = set([words[1].strip().title()])
    
singlets = 0
most = 0
for name in counts:
    if len(counts[name]) == 1:
        singlets += 1
    if len(counts[name]) > most:
        most = len(counts[name])
        person = name
        
print("{} appears most often: {} times".format(person, most))
print("{} people appear once".format(singlets))