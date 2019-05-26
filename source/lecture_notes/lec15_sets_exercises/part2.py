if __name__ == '__main__':
    data_file = input('Data file name: ').strip()
    print(data_file)
    prefix = input('Prefix: ').strip()
    print(prefix)

    names = set()
    movies = set()
    for line in open(data_file):
        m = line.split("|")
        name = m[0].split(',')[0].strip()
        if len(name) > 0:
            names.add( name ) 
    
    count = 0
    for n in names:
        if n.startswith(prefix):
            count += 1
 
    print("{} last names".format(len(names)))
    print("{} start with {}".format(count, prefix))

