Lecture 6 --- Exercises
=======================


Solutions to the problems below must be sent to Submitty for grading.
A separate file must be submitted for each problem. These must be
submitted by 09:59:59 am on Friday, February 1st.

#. Consider the following boolean expressions:

   ::

       a = 1.6
       b = -1.7
       c = 15
       s = 'hi'
       t = "good"
       u = "Bye"
       v = "GOOD"
       w = "Bye"
       y = 15.1

       a < b             # A
       a < abs(b)        # B
       a >= c            # C
       s < t             # D
       t == v            # E
       u == w            # F
       b < y             # G

   Upload a text file to Submitty containing only the labels (A, B, C,
   etc.) of the lines that evaluate to ``True``.  Each line of the
   uploaded file should contain a single capital letter and the
   letters should be in alphabetical order.

#. Consider the following boolean expressions:

   ::

       x = 15
       y = -15
       z = 32
       x == y and y < z        # A
       x == y or y < z         # B
       x == abs(y) and y < z   # C
       x == abs(y) or y < z    # D
       not x == abs(y)         # E
       not x != abs(y)         # F

   Upload a text file to Submitty containing only the labels (A, B, C,
   etc.) of the lines that evaluate to ``True``.  Each line of the
   file should contain a single capital letter and the letters should
   be in alphabetical order.

#. So far we have assumed all input to our programs is correct.  In
   practice, however, programs must do extensive error checking.  Here
   is a slightly-contrived problem to illustrate this: Write a short
   program that asks the user to input two numbers where one of them
   must be greater than 10 and the other must be less than or equal
   to 10.  It does not matter which is which.  If both inputs are
   greater than 10, the program should output the error message "Both
   are above 10."  If both are less than or equal 10, the program
   should output the message "Both are below 10."  If one of the
   numbers is above 10 and the other is less than or equal to 10, no message
   should be output.  Regardless of any messages, the program should then 
   output the average of
   the two numbers, accurate to 2 decimals.  This program must use one
   ``if``, one ``elif``, and **no** ``else``.  Note: just like in HW 1, the
   program should output a value immediately after reading it. Also, if you
   are having problems matching our output format, explore the difference
   between the output of the following two lines:
   
   ::

      print("{:.2f}".format(112.099))
      print(round(112.099, 2))

   Here are two examples of how your program might look when run from
   the interpreter:

   ::

      Enter the first number: 17.1
      17.1
      Enter the second number: 13.45
      13.45
      Both are above 10.
      Average is 15.28

   and

   ::

      Enter the first number: 4.7
      4.7
      Enter the second number: 15.5
      15.5
      Average is 10.1
