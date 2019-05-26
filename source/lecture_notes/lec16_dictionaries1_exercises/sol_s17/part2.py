imdb_file = input("Enter the name of the IMDB file ==> ").strip()
print(imdb_file)

counts = dict()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    
    if name in counts:
        counts[name] += 1
    else:
        counts[name] = 1
    
singlets = 0
most = 0
for name in counts:
    if counts[name] == 1:
        singlets += 1
    if counts[name] > most:
        most = counts[name]
        person = name
        
print("{} appears most often: {} times".format(person, most))
print("{} people appear once".format(singlets))
