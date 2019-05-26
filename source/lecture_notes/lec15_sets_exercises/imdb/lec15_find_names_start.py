'''
This is the start to the solution to the problem of find all people
named in the internet movide database.  

One important note.  In opening the file we need to specify the
encoding the text.  The default is what's known as utf-8, but this
only handles English characters well.  For the IMDB file, we need to
open with a more language-independent, international standard.  This
is 'ISO-8859-1'.

As we will use the time.time() function to measure how long our
computation takes.  This function tells the seconds since an "epoch",
which is 1/1/1970 on Unix-based systems (including Macs and Linux
machines) and 1/1/1601 on Windows machines.  By recording in the
software the time before the calculations start, the time when the
calculations end, and subtracting we get the elapsed time.
'''
import time


imdb_file = input("Enter the name of the IMDB file ==> ").strip()
name_set = set()
count = 0
start = time.time()
for line in open(imdb_file, encoding = "ISO-8859-1"):
    words = line.strip().split('|')
    name = words[0].strip()
    count += 1
    name_set.add(name)
    if count % 1000 == 0:
        print ("Tested {} lines so far.".format(count))
        
end = time.time()
print("I found {} unique names in {} lines for file {}".format(len(name_set), count, imdb_file))
print("This run took {:.4f} seconds.".format(end-start))
