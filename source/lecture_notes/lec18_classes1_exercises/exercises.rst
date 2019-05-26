Lecture 18 --- Exercises
========================

Solutions to the problems below must be sent to Submitty for
automatic scoring.  A separate file must be submitted for each problem.
Solutions must be submitted by 09:59:59 am on Friday, March 29.

#. Starting from the ``Point2d.py`` file you download from the
   Course Materials section of the Submitty Website, please do the following:

   #. Write a new ``Point2d`` method called :func:`scale` that takes as an
      input argument a ``Point2d`` object (``self``) and a numerical
      value (int or float) and multiples both the ``x`` and ``y``
      attributes by this value.

   #. Write a new ``Point2d`` method called :func:`dominates` that two
      takes two ``Point2d`` objects and returns ``True`` if and only
      if the x coordinate of the first object is greater than that of
      the second object and the y coordinate of the first object is
      greater than that of the second object.

   #. The code to test these functions is commented out in the main
      code area. Please remove this commenting, test your code, and
      submit your resulting ``Point2d.py`` file.  Call it ``Point2d_q1.py``.

#. Copy your resulting file from the first question to a new file,
   perhaps called ``Point2d_q2.py``.

   #. Write and test the implementation of method :func:`__str__`
      which returns a string created from the values of a ``Point2d``
      object. For our purposes this is mostly used to create a string
      that can be printed. Make sure you have this working before
      you proceed to the other parts of this exercise because they
      depend on it.

   #. Write the implementation of the subtraction method :func:`__sub__`
      for the ``Point2d`` object. Uncomment the code in the main area
      and test this in Wing IDE 101.

   #. Write the implementation of the method :func:`__mul__` which is
      like the :func:`scale` function you wrote for part 1, but it creates
      a new ``Point2d`` object.

   #. Write the implementation of the method :func:`__eq__` which
      returns ``True`` if and only if the two ``Point2d`` objects have
      exactly the same ``x`` and ``y`` values.

   For each of these you should look at the commented out main code in
   the ``Point2d.py`` file you were provided to see how these
   methods should be used. Uncomment this code, test your methods,
   and upload to Submitty when you are done.

#. Open the file ``pokemon.py`` you download from the
   Course Materials section of the Submitty Website. This file initially
   contains just the testing code. Write the definition for the ``Pokemon``
   class with all necessary methods, so that all tests run successfully:

   #. The initializer which takes four input parameters:
      the object itself (``self``), the name of the Pokemon (string),
      the board size (2-tuple of integers, corresponding to the row and
      column), and the initial position of the pokemon (also a 2-tuple
      of integers). If no initial position is specified
      when creating a Pokemon object, :math:`(0, 0)` should be implied.

   #. The function to move the pokemon to the next cell in one of the
      directions ("N", "E", "S", or "W"). The pokemon should not go off
      the board.

   #. The function to represent a ``Pokemon`` object as a string, e.g.,
      if ``pmon`` is a ``Pokemon`` object, ``str(pmon)`` would
      return something like ``Celebi is at row 4, column 6.``.
