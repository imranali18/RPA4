Lecture 21 --- Exercises
========================

Solutions to the problems below must be sent to Submitty for
automatic scoring. A separate file must be submitted for each problem.
Solutions must be submitted by 09:59:59 am on Tuesday, April 9. Download
the file ``lecture21_files.zip`` from the Course Materials section on Submitty.

#. The file ``insert_sort.py`` contains an implementation of the
   insertion sort algorithm. It includes a call to :func:`print` function.
   What are the outputs of this statement? Submit a text file
   showing the output.

#. The file ``merge.py`` contains an implementation of the
   :func:`merge` function that is the heart of merge sort.  We only
   consider :func:`merge` here and not the full sort. Modify the :func:`merge`
   function so that if the same value appears in both lists then only
   one copy of the value is in the final merged list. You may assume
   that each contains no duplicates. Work within the context of the
   merge function itself, meaning that you should not use a set and
   you should not use an extra list. You need to only change a few
   lines of code.

   For example, if the two lists are:

   ::

       L1 = [2, 7, 9, 12, 17, 18, 22, 25]
       L2 = [1, 5, 6, 8, 13, 14, 15, 18, 19, 23, 25]

   Then the result ``merge(L1, L2)`` should be the list:

   ::

       [1, 2, 5, 6, 7, 8, 9, 12, 13, 14, 15, 17, 18, 19, 22, 23, 25]

   Do not change the name of the function and do not change the name
   of the file. On Submitty, we will run code that imports
   ``merge.py`` and calls function :func:`merge` passing two lists as
   arguments.

