Lecture 8 --- Exercises
=======================


Solutions to the problems below must be sent to Submitty for grading.
A separate file must be submitted for each problem. These must be
submitted by 09:59:59 am on Tuesday, February 12.

#. Upload a text file showing the output of the following code to
   Submitty. As usual, you should try to predict the output by hand.

   ::

      l1 = [6, 12, 13, 'hello']
      print(l1[1], l1[-2])
      l1.append( 15)
      print(len(l1))
      print(len(l1[3]))
      l1.pop(3)
      l1.sort()
      l1.insert(2, [14, 15])
      l1[3] += l1[4]
      l1[3] += l1[2][1]
      print(l1[3])
      l1.pop()
      l1[2].remove(14)
      print(l1)

#. Write a short Python program that starts with the list:

   ::

      values = [14, 10, 8, 19, 7, 13]

   (The above statement list should be the first line of your
   program.)  Then add code that does the following steps:

   #. Reads an integer, prints it (as we have done for input when using
      Submitty), and appends it to the end of ``values``.

   #. Reads another integer, prints it and inserts it at index
      location 2 of ``values``.

   #. Prints the integer at index 3 of ``values`` and prints the
      integer at index -1 of ``values``, both on one line with a space between them.

   #. Prints the difference between the maximum and minimum of the
      integers in ``values``.

   #. Prints the average of the integers in ``values``, accurate to
      one decimal place. This must use the functions :func:`sum` and
      :func:`len`. 

   #. Prints the median of the numbers in ``values``.  Since the list
      is even length (a fact that you are allowed to use, just for this
      exercise), this is the average of the two middle integers after
      ``values`` is sorted.

   Here is an example of running our solution (as it would look on Submitty):

   ::

     Enter a value: 15
     Enter another value: 23
     8 15
     Difference: 16
     Average: 13.6
     Median: 13.5


   
