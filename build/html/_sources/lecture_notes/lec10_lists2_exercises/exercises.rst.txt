Lecture 10 --- Exercises
========================

.. |CO2| replace:: CO\ :sub:`2`\

Solutions to the problems below must be sent to Submitty for grading.
A separate file must submitted be for each problem. 
Due date is 09:59:59 am on Wednesday, February 20th.

#. Submit a text file showing the output of the following code:

   ::

      L1 = [1, 5, [5, 2], 'hello']
      L2 = L1
      L3 = L1.copy()
      L2.append(4)
      L1.append(3)
      print(L1)
      print(L2)
      print(L3)

#. Submit a text file showing the output of the following code:

   ::

      def head_and_tail(L):
          from_back = L.pop()
          from_front = L.pop(0)
          L.append(from_front)
          L.insert(0, from_back)

      L1 = [[1, 2], 3]
      L3 = L1.copy()
      L2 = L1
      L2[-1] = 5
      L2.insert(1, 6)
      head_and_tail(L1)

      print(L1[0], L1[-1], len(L1))
      print(L2[0], L2[-1], len(L2))
      print(L3[0], L3[-1], len(L3))

#. The solution to this problem and the two that follow should start
   with the assignment:

   ::

      co2_levels = [ 320.03, 322.16, 328.07, 333.91, 341.47, \
                     348.92, 357.29, 363.77, 371.51, 382.47, 392.95 ]

   Write a Python program that prints the number of values that are greater
   than the average of the list.  For this you may use Python's
   :func:`sum` and :func:`len` functions and you must use a ``for`` loop. Do
   NOT use :func:`range`, however, and do not use indexing.

   Your output should simply be:

   ::

      Average: 351.14
      Num above average: 5

#. Suppose we discovered that the measurement of |CO2| values was
   uniformly too low by a small fraction ``p``. Write a function that
   increases each value in ``co2_levels`` by the fraction ``p``. (In
   other words, if ``x`` is the value before the increase then
   ``x * (1 + p)`` is the value after.) For this problem you need to use
   :func:`range`, :func:`len`, and indexing. Start by asking the user for the
   percentage. Output the first and last values of the revised list.
   Your program should end with the lines:

   ::

      print('First: {:.2f}'.format(co2_levels[0]))
      print('Last: {:.2f}'.format(co2_levels[-1]))
   
   Here is an example of running your program:

   ::

      Enter the fraction: 0.03
      First: 329.63
      Last: 404.74

#. Write a function called :func:`is_increasing` that returns ``True`` if
   the values in the list it is passed are in increasing order and
   ``False`` otherwise.  Use a ``for`` loop and indexing to accomplish
   this.  Test the function with the following main code:

   ::

      print('co2_levels is increasing: {}'.format(is_increasing(co2_levels)))
      test_L1 = [15, 12, 19, 27, 45]
      print('test_L1 is increasing: {}'.format(is_increasing(test_L1)))
      test_L2 = ['arc', 'circle', 'diameter', 'radius', 'volume', 'area']
      print('test_L2 is increasing: {}'.format(is_increasing(test_L2)))
      test_L3 = [11, 21, 19, 27, 28, 23, 31, 45]
      print('test_L3 is increasing: {}'.format(is_increasing(test_L3)))

   These should be the only :func:`print` function calls in the code
   you submit.

