Lecture 16 --- Exercises
========================

Solutions to the problems below must be sent to Submitty for
automatic scoring. A separate file must be submitted for each problem.
Solutions must be submitted by 09:59:59 am on Friday, March 22.

#. Write a Python program that forms a dictionary called ``countries``
   that associates the population with each of the following
   countries (in millions):

   -  Algeria 37.1

   -  Canada 3.49

   -  Uganda 32.9

   -  Morocco 32.7

   -  Sudan 30.9

   -  Canada 34.9   # a correction to the error above.

   and then prints the length of the ``countries`` dictionary, the
   sorted list of the keys in ``countries``, and the sorted list of the
   values in ``countries``. There should be six assignment statements
   in your program (seven if you include initializing the dictionary)
   and three lines of output from your program.
   Please initialize your dictionary using :func:`dict()` rather than ``{}``.

#. Our solution to the IMDB problem thus far has not actually told us
   who is the busiest individual in the Internet Movie Database.
   Your job in this part is to complete this task. Starting from the
   code produced in class, which will be immediately posted on the
   Course Website (in the *Code written in class* area), write a
   program that finds and prints the name of the individual who
   appears the most times in the IMDB file you are given. Also, count
   and output the number of individuals who appear only 1 time in the
   IMDB.

   For example. if the answer was ``Thumb, Toni`` and this
   person had appeared 100 times, and if 2,000 people had only
   appeared once, then your output would be:

   ::

      Enter the name of the IMDB file ==> imdb_data.txt
      Thumb, Toni appears most often: 100 times
      2000 people appear once

   We strongly suggest that you test your solution on the
   ``hanks.txt`` dataset first! We will test on multiple files. You
   do not need to worry about the possibility of a tie for the most
   commonly occurring name. Please initialize your dictionary using
   :func:`dict()` rather than ``{}``.
  
   
