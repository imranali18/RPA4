Lecture 17 --- Exercises
========================

Solutions to the problems below must be sent to Submitty for
automatic scoring. A separate file must be submitted for each problem.
Solutions must be submitted by 09:59:59 am on Tuesday, March 26.

#. What is the output of the following code?

   ::

      d1 = dict()
      l1 = [5, 6, 7]
      d1['car'] = l1
      d1['bus'] = l1.copy()
      l1.append([8, 9])
      d1['truck'] = d1['bus']
      d1['bus'].append(10)
      d1['truck'].pop(0)
      print("list:", l1)
      for v in sorted(d1.keys()):
          print("{}: {}".format(v, d1[v]))

#. Write a Python program that finds the name of the movie in our
   Internet Movie Database that involved the most *unique* individuals. Print
   the number of individuals on one line and the name of the movie on 
   the next line. You do not need to consider the possibility of
   ties and you should assume all actors and movies have the correct 
   capitalization. Finally, print the number of movies involving only one
   individual (yes, there are such movies). For example, if the name
   of the movie is *Ben Hur* with 2,342 individuals, and 165 movies
   have only one individual then the output from your program will
   look like:

   ::

      Enter the name of the IMDB file ==> imdb_data.txt
      2342
      Ben Hur
      165

   Note that you only need to create one dictionary for this
   exercise. Start by planning the organization of this dictionary
   and thinking through how you are going to use it. As with Lecture Exercises
   16, make sure you use *dict()* to initialize your empty dictionary.
