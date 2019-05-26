imdb_file = input("Enter the name of the IMDB file ==> ").strip()
count_list = []
for line in open(imdb_file, encoding="utf-8"):
    words = line.strip().split('|')
    name = words[0].strip()
    found = False
    count_list.append(name)

count_list.sort()

index = 0
while index < len(count_list):
    name = count_list[index]
    count = 0
    while count_list[index] == name and index < len(count_list):
        count += 1
        index += 1
    print("{} appeared in {} movies".format(name, count), flush=True)
