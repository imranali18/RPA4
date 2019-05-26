Lecture 15 --- Exercises
========================

Solutions to the problems below must be sent to Submitty for
automatic scoring.  A separate file must be submitted for each problem.
Solutions must be submitted by 09:59:59 am on Tuesday, March 19.

#. What is the output of the following Python code? Write the answer by
   hand before you type it into the Python interpreter.  One thing
   that will be hard to guess is the order of the sets, especially
   when the set mixes integers and strings.  Therefore, you pretty
   much have to run the code to make sure you have the order right.
   (At the moment, our use of Submitty is not sophisticated enough to
   allow random order.)  This means you get the points almost for
   free, but you should make the effort to be sure you understand what
   is happening.

   ::

       s1 = set([0, 1, 2])
       s2 = set(range(1, 9, 2))
       print('A:', s1.union(s2))

       print('B:', s1)

       s1.add('1')
       s1.add(0)
       s1.add('3')
       s3 = s1 | s2
       print('C:', s3)

       print('D:', s3 - s1)

   Note that this example does NOT cover all of the possible set
   operations. You should generate and test your own examples to ensure
   that you understand all of the basic set operations.

#. Write a Python program that asks the user for two strings:  (1) the
   name of a file formatted in the same way as the IMDB data, and (2)
   a string that is the start of a last name.  The program should
   output the number of different last names that are in the file and
   it should output the number of different names that start with the
   string.  Your program *must* use a :func:`set` and you may / are
   encouraged to start from
   the code written during lecture.

   We define the last name to be everything up to the first comma in the
   name.  (Some names will not have commas in them, so be careful to
   avoid adding empty last names to the set.)   For example:

   ::

       Downey Jr., Robert | Back to School |      1986 
       Downey Sr., Robert   | Moment to Moment  | 1975
       Downey, Elsie    | Moment to Moment     |  1975

   would result in three different last names, ``Downey Jr.``,
   ``Downey Sr.``, and ``Downey``.

   Here is one example of running our solution:

   ::
   
      Data file name: imdb_data.txt
      Prefix: Down
      48754 last names
      10 start with Down
 
   Before uploading your Python file to Submitty you should test using
   the data files (or restricted versions of them!)  we provided for
   Lecture 15 on the Course Materials page on Submitty. On Submitty we will test with
   different files and examples.
