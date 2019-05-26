Lecture 20 --- Exercises
========================

Solutions to the problems below must be sent to Submitty for
automatic scoring.  A separate file must be submitted for each problem.
Solutions must be submitted by 09:59:59 am on Friday, April 5.

For both of these exercises download the file ``lec20_ex.zip`` from
the Course Materials page on Submitty. It includes a data file and
``lec20_ex_start.py``. You start from the latter for both exercises.
You will notice that the main code in this file requests the name of a
data file from the user, opens and reads the file to form a list of
values, and then in a loop requests several different values to search
for, outputting the result of the function call for each.

#. Write a Python function called :func:`linear_search` that is given two
   arguments:  a value ``x`` and a list ``L``. The function must
   return the list index of the first location of ``x`` in ``L``.  If
   ``x`` is not in ``L`` the function must return -1.  You may use any
   Python ``list`` functions you wish.


#. What if the list is already sorted? Write a modified version of
   :func:`linear_search` that returns the index of the first instance of
   ``x`` or the index where ``x`` should be inserted if it is not in
   ``L``. For example, in the list:

   ::

         L = [1.3, 7.9, 11.2, 15.3, 18.5, 18.9, 19.7]

   the call:

   ::

         linear_search(11.9, L)

   should return 3, while the call:

   ::

         linear_search(20.5, L)

   should return 7. You must not use binary search (even though that
   would be faster --- this is an exercise) and you must use either a
   ``for`` or a ``while`` loop.



