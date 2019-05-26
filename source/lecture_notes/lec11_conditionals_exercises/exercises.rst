Lecture 11 --- Exercises
========================

Solutions to the problems below must be sent to Submitty for grading.
A separate file must be submitted for each problem. Solutions must be
submitted by 09:59:59 am on Friday February 22.

#. Suppose you have a tuple that stores the semester and year a course
   was taken, as in:

   ::

       when = ('Spring', 2015)

   Write a function called :func:`earlier_semester` that takes two
   such tuples as arguments and returns ``True`` if the first tuple
   represents an earlier semester and ``False`` otherwise. The
   possible semesters are ``'Spring'`` and ``'Fall'``. (Just to be
   clear, Fall 2013 is later than Spring 2013.) Test it using the
   following main code (you can cut-and-paste from the browser), which
   should be your only print() function calls:

   ::
      
       # Insert your function def here...

       w1 = ('Spring',2015)
       w2 = ('Spring',2014)
       w3 = ('Fall', 2014)
       w4 = ('Fall', 2015)
       print("{} earlier than {}? {}".format(w1, w2, earlier_semester(w1, w2)))
       print("{} earlier than {}? {}".format(w1, w1, earlier_semester(w1, w1)))
       print("{} earlier than {}? {}".format(w1, w4, earlier_semester(w1, w4)))
       print("{} earlier than {}? {}".format(w4, w1, earlier_semester(w4, w1)))
       print("{} earlier than {}? {}".format(w3, w4, earlier_semester(w3, w4)))
       print("{} earlier than {}? {}".format(w1, w3, earlier_semester(w1, w3)))

#. Suppose three siblings, ``Dale``, ``Erin``, and ``Sam``, have
   heights ``hd``, ``he`` and ``hs``, respectively. Write a program
   that reads in integer values of their heights and outputs
   the ordering from tallest to shortest. (For simplicity of
   this exercise, you may assume that the three heights you will be
   given are all different.) Try writing your solution using nested
   if statements and then try re-writing it without nested if statements;
   either is acceptable on Submitty and trying both is good practice.
   Here is an example of the output the way it would look on Submitty:

   ::

      Enter Dale's height: 124
      Enter Erin's height: 112
      Enter Sam's height: 119
      Dale
      Sam
      Erin
