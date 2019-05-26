Lecture 5 --- Exercises
=======================

Solutions to the problems below must be sent to Submitty for grading.
A separate file must submitted for each problem. These must be
submitted by 09:59:59 am on Tuesday, January 29.

#. Write a function called :func:`convert2fahren` that takes a Celsius
   temperature and converts it to Fahrenheit, returning the answer.
   Write code that calls the function three times to convert
   temperatures 0, 32, and 100 to Fahrenheit, printing the result each
   time.  To keep things simple for these exercises, the output should
   be:

   ::

       0 -> 32.0
       32 -> 89.6
       100 -> 212.0

   Submitty will check that a function exists with exactly the given
   name, that it does the calculation, and that it is called three
   times.
       
#. Write a function called :func:`frame_string` that takes a string as an
   argument.  Its job is to print that string with a frame around it,
   just like in Lab 2.  Unlike the other functions we have written,
   :func:`frame_string` does not need and therefore should not have a
   ``return`` statement.  Write code to call the function two times.
   For the first call pass the string ``Spanish Inquisition``.  For the
   second call, pass the string ``Ni``.  Print a blank line between
   calls.  The output should be:

   ::

       *************************
       ** Spanish Inquisition **
       *************************

       ********
       ** Ni **
       ********

   In addition to checking the output, we will check that you wrote
   a function called :func:`frame_string` and that your code calls this
   function twice.


For extra practice, but not to be uploaded to Submitty, solve the
following:

#.  Add code to your first function that has a second parameter which
    is the minimum temperature in Fahrenheit.  If the converted
    temperature is less than this, use this minimum value.  Write code
    to run this modified function using the value 159.67 and test that
    it works correctly.  

#.  Add code to the second program you wrote to print out the
    result of the calls to :func:`frame_string`.  The output should be the value
    ``None``.  This is a special Python value that indicates "there is
    no value".  The most common example of using ``None`` is the
    result of a function that has no ``return`` statement.
