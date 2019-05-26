Lecture 12 --- Exercises
========================

Solutions to the problems below must be sent to Submitty for grading.
A separate file must be submitted for each problem. Solutions must be
submitted by 09:59:59 am on Tuesday, February 26.

#. The following simple exercise will help you understand loops better.
   Show the output of each of the following pairs of ``for`` loops. The
   first two pairs are nested loops, and the third pair is formed by
   consecutive, or *sequential*, loops. Submit a single text file
   containing three lines, each with an integer on it.

   ::

       # Version 1
       total = 0
       for i in range(10):
           for j in range(10):
               total += 1
       print(total)

   ::

       # Version 2
       total = 0
       for i in range(10):
           for j in range(i + 1, 10):
               total += 1
       print(total)

   ::

       # Version 3
       total = 0
       for i in range(10):
           total += 1
       for j in range(10):
           total += 1
       print(total)


#. Write a function called :func:`first_day_greater` that takes two lists,
   ``L1`` and ``L2``, 
   representing the daily measured weights of rat 1 and rat 2,
   respectively, and returns the index of the first day for which the
   weight for the first rat is greater than the weight of the second
   rat.  If there are no such days then the function should return
   -1.  You may NOT assume that ``L1`` and ``L2`` are the same length.

   Use the following to test your program:

   ::

      if __name__ == "__main__":
          L1 = [15.1, 17.3, 12.3, 16.4]
          L2 = [15.0, 17.7, 12.5, 16.9]
          print("Test 1: {}".format(first_day_greater(L1, L2)))
          L2 = [15.6, 17.9, 18.2, 16.5, 12.7]
          print("Test 2: {}".format(first_day_greater(L1, L2)))
          L2 = [15.9, 18.8, 11.4]
          print("Test 3: {}".format(first_day_greater(L1, L2)))


#. Write a function called :func:`find_min` that takes a list of lists and
   returns the minimum value across all lists. Test it with the
   following:

   ::

      if __name__ == "__main__":
          v = [[11, 12, 3], [6, 8, 4], [17, 2, 18, 14]]
          print("Min of list v: {}".format(find_min(v)))
          u = [['car', 'tailor', 'ball'], ['dress'], ['can', 'cheese', 'ring'], \
                    ['rain', 'snow', 'sun']]
          print("Min of list u: {}".format(find_min(u)))


