imdb_file = input("Enter the name of the IMDB file ==> ").strip()
count_list = []
for line in open(imdb_file, encoding="utf-8"):
    words = line.strip().split('|')
    name = words[0].strip()
    found = False
    for pair in count_list:
        if pair[0] == name:
            pair[1] += 1
            found = True
            break
    if not found:
        new_pair = [name, 1]
        count_list.append(new_pair)

for pair in count_list:
    print("{} appeared in {} movies".format(pair[0], pair[1]))
