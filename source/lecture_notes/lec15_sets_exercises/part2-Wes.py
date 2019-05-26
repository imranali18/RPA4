'''
This is the start to the solution to the problem of find all people
named in the internet movide database.  

As we will use the time.time() function to measure how long our
computation takes.  This function tells the seconds since an "epoch",
which is 1/1/1970 on Unix-based systems (including Macs and Linux
machines) and 1/1/1601 on Windows machines.  By recording in the
software the time before the calculations start, the time when the
calculations end, and subtracting we get the elapsed time.
'''
import time


imdb_file = input("Data file name: ")
print(imdb_file)
imdb_file = imdb_file.strip()

last = input("Prefix: ")
print(last)
last = last.strip()

name_list = set()
last_name_list = set()

ctr = 0
start = time.time()
# Patched by Konstantin Kuzmin on 20190317
# "open(imdb_file)" replaced with "open(imdb_file, encoding="utf-8")"
# to avoid crashing on imdb_data.txt
for line in open(imdb_file, encoding="utf-8"):
    words = line.strip().split('|')
    fullname = words[0].strip()
    lastname = fullname.split(',')
    lastname = lastname[0].strip()
    name_list.add(lastname)
    if lastname.find(last) == 0:
        last_name_list.add(lastname)
        
    '''
    ctr += 1
    if ctr % 1000 == 0:
        print(ctr)
    '''

end = time.time()
print('{} last names'.format(len(name_list)))
print('{} start with {}'.format(len(last_name_list), last))
'''
for name in name_list:
    print(name)
'''