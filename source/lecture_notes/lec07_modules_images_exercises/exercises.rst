Lecture 7 --- Exercises
=======================


Solutions to the problems below must be sent to Submitty for grading.
A separate file must be submitted for each problem. These must be
submitted by 09:59:59 am on Tuesday, February 5th.

#. What is the output from the following code?  Note that we did not
   cover all of these techniques in class, so you might need to do
   some exploration on your own.

   ::

      def hmmm(x):
          if x[0] > x[1]:
              return (x[1], x[0])
          else:
              return x
      
      s = ('a', 'b')
      t = (1, 2, 3)
      u = (4, 5, 2)
      print(t[1] + u[0])
      print(t + u)
      print(s[1] * t[2])
      print(hmmm(u))
      print(hmmm((5, 2, 3)))


#. Write a function called :func:`add_tuples` that takes three tuples,
   each with two values, and returns a single tuple with two values
   containing the sum of the values in the tuples.  Test your function
   with the following calls:

   ::

      print(add_tuples((1, 4), (8, 3), (14, 0)))
      print(add_tuples((3, 2), (11, 1), (-2, 6)))

   Note that these two lines of code should be at the bottom of your
   program.  This should output:

   ::

      (23, 7)
      (12, 9)
