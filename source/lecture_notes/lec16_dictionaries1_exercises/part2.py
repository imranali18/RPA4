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

'''
for n in counts:
    print("{}: {}".format(n,counts[n]))
print('\n-------\n')
'''

max_count = 0
max_name = ''
appeared_once = 0
for n in counts:
    if counts[n] > max_count:
        max_count = counts[n]
        max_name = n
    if counts[n] == 1:
        appeared_once += 1

print("{} appears most often: {} times".format(max_name, max_count))
print("{} people appear once".format(appeared_once))
