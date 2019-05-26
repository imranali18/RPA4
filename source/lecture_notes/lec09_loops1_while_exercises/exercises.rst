Lecture 9 --- Exercises
=======================

Solutions to the problems below must be sent to Submitty for grading.
A separate file must submitted for each problem. Each problem
requires you to use a *while* loop. As a whole, this exercise set is a
bit longer than previous ones because loops are so important and
require so much practice. Solutions must be submitted by 09:59:59 am on
Friday, February 15.

#. Write a program that asks the user for a single integer ``n`` and
   prints the non-negative multiples of 3 that are less than ``n``.
   Here is an example run of the program on Submitty:

   ::

      Enter a positive integer: 12
      0
      3
      6
      9

#. The following list represents the population of New York State (in
   hundreds of thousands of people) for the US Census in 1790, 1800,
   1810, etc., all the way through 2010:

   ::

      census = [340, 589, 959, 1372, 1918, 2428, 3097, 3880, 4382, 5082, \
                  5997, 7268, 9113, 10385, 12588, 13479, 14830, 16782, \
                  8236, 17558, 17990, 18976, 19378]

   Copy and paste this list into the start of a new program file.
   Then write code to find the average percentage change from one
   decade to the next, across all decades. For example, the change
   from 1790 to 1800 is (589 - 340) / 340 * 100 = 73.2% and the change
   from 1800 to 1810 is (959 - 589) / 589 * 100 = 62.8% so the average
   across just these two decades is 68.0%. The output of your program
   would then simply be:

   ::

      Average = 68.0%

   Your answer will be different because it is taken from all
   decades.

#. Write a program that inputs integer values that the user types
   until the user types a 0. Each value (other than 0) should be
   stored in a list. The program should then output the minimum,
   maximum, and average of the values in the list. Your program must
   start by creating an empty list to store the values. Here's an
   example of how it might look on Submitty:

   ::

      Enter a value (0 to end): 5
      Enter a value (0 to end): 3
      Enter a value (0 to end): 11
      Enter a value (0 to end): 0
      Min: 3
      Max: 11
      Avg: 6.3
