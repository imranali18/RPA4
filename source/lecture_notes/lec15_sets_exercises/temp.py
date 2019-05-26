data_file = input('Data file name: ').strip()
print(data_file)
prefix = input('Prefix: ').strip()
print(prefix)

names = set()
for line in open(data_file, encoding = "ISO-8859-1"):
    m = line.strip().split("|")[0].strip()
    if not ',' in m:
        print(m)
