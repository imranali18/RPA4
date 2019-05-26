Lecture 3 — Exercises
=====================

Overview
--------

Solutions to the problems below must be sent to Submitty for grading.
A separate file must submitted for each problem, as practiced in
Lab 1.  For these Lecture 3 exercises, you must submit your
solutions before Wednesday, January 23 at 11:59:59 pm. Starting with Lecture 4, 
you will be required to submit your lecture exercises within 24 hours
of the start of lecture.  Students are
welcome to work on these problems in small groups, but each student
should write the final version of their solutions independently to
assure themselves that they understand the material.

Problems
--------

#. Which of the following are valid strings?  Upload a text file to
   Submitty that contains just the variable names that are assigned to
   strings that are correct.  For example if only the first two were
   correct your file would contain *s0* on the first line and *s1* on the
   second.

   ::

       >>> s0 = "Sheldon Cooper's apartment is in Pasedena"

       >>> s1 = 'This cheese shop's cheese is all gone"

       >>> s2 = """We are
       "The Knights of the Round Table"
       """

       >>> s3 = "Toto, I said,\n"We aren't in Kansas, anymore!"


       >>> s4 = 'Have you seen the "Final Five"'s picture?'


       >>> s5 = "Have you seen the 'Final Five''s picture?"

#. Submit a Python file that includes a single line of code that prints
   25 ``'*'`` characters followed by 25 ``'+'`` characters, with no
   space in between.  It must, of course, use the :func:`print` function.
   The two characters must appear in your code *much less* than 25
   times - at most three each!

#. Write a program that assigns value *4* to variable ``x``,
   value *2* to variable ``y``, and then uses exactly *three*
   :func:`print` function calls to generate the output below (four lines,
   with the second line blank).  The :func:`print` calls must use
   variables ``x`` and ``y`` rather than values *4* and *2*.  The
   trick is to change the assignment of ``sep`` and ``end``
   parameters in the call to :func:`print`.  Character *4* is the
   first character on the 1st, 3rd, and 4th lines of output.

  ::

    4 2

    4,2
    42

