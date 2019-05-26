Lecture 4 --- Exercises
=======================


Solutions to the problems below must be sent to Submitty for grading.
A separate file must be submitted for each problem. These must be
submitted by 23:59:59 pm on Monday, January 28.


#. Write a program that assigns a string to the variable called
   ``phrase`` and then transforms ``phrase`` into a hashtag. In other
   words, all words in ``phrase`` are capitalized, all spaces are
   removed, and a ``#`` appears in front. Store the result in a
   variable called ``hashtag``. Then print the value of both
   ``phrase`` and ``hashtag``. Your program should start with:

   ::
 
      phrase = 'Things you wish you knew as a freshman'

   and the output from the program (using :func:`print` function
   calls) should be:

   ::

      The phrase "Things you wish you knew as a freshman"
      becomes the hashtag "#ThingsYouWishYouKnewAsAFreshman"

   Note that the output includes the quotation marks.

#. One of the challenges of programming is that there are often many
   ways to solve even the simplest problem.  Consider computing the
   area of the circle with the standard formula:

   .. math:: a(r) = \pi r^2

   Fortunately, we now have ``pi`` from the *math* module, but to
   compute the square of the radius we can use ``**`` or
   :func:`pow` or we can just multiply the radius times itself. To
   print the area accurate to only a few decimal places we can now use
   the string :func:`format` method or the :func:`round` built-in
   function, which includes an optional second argument to specify the
   number of decimal places.

   Write a short Python program that computes and prints the areas of
   two circles, one with radius 5 and the other with radius 32. Your
   code must use ``**`` once and :func:`pow` once and it must use
   :func:`format` once and :func:`round` once.  The output should be
   exactly:

   ::

       Area 1 = 78.54
       Area 2 = 3216.99
