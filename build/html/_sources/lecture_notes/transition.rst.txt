Transition to the next class - Data Structures
===============================================


Overview
--------

If you are continuing on your journey in Computer Science, here are
some suggestions for you.

-  The next class in the sequence will introduce you to completely new
   concepts, building on the concepts learnt in this class.

-  Make sure you are very comfortable with the concepts we learnt
   here. Review labs and homeworks, make sure you can solve them
   pretty easily.

-  Install a working environment in C++, which is the language you
   will be using in the next class. 

-  Review C++ syntax before you take your next class. Make sure you
   develop:

   - Skills to solve the CS-1 level problems in C++.
   - Skills to debug C++ programs. 


   Students who wrote basic C++ programs over the break did well in 
   Data Structures. It also helps solidify your algorithmic problem
   solving skills.

-  You can also review the first few labs in Data Structures if you
   wish and work on those in advance:

   http://www.cs.rpi.edu/academics/courses/fall18/csci1200/calendar.php

In this document, there are some suggestions to help you get ready for
your next class.

Learning C++
-------------

You are not learning C++ from scratch. Many basic constructs are very
similar in C++, but there are differences too. Here are some sources
that were highly recommended:

- Tutorial on C++:

  http://www.cplusplus.com/doc/tutorial/

- See also this for a quick overview of syntax:

  http://www.cs.rpi.edu/academics/courses/fall17/csci1200/other_information.php

- Another good site for video tutorials:

  https://www.youtube.com/playlist?list=PLAE85DE8440AA6B83

Go through the tutorial and the videos. Make sure to write many
programs.

Differences between Python and C++
-----------------------------------

Here are a few first things to notice between the two:

- C++ is a compiled statically typed language. This means that
  variables need to be defined with a data type first, and the data
  type cannot be changed. 

- Programs cannot be run until compiled. If you have a syntax error,
  the compiler will not produce an executable until you resolve all
  syntax errors.  

- In C++, many new errors will be checked at compile time, like trying
  to add a string and an integer. As Python is dynamically typed, you
  are used to resolving such errors at run time. This means, you will
  spend more of your time in fixing compilation errors in C++ than in
  Python. Hence, learn to write programs in small steps, test and
  expand. 

- Syntax differences: each line in a program must end with a semicolon
  and each block must be delimited by curly brackets.

- Be aware of the scope of local/global variables. Generally using our
  convention of passing variables to functions only as arguments and
  returning the result will help you a lot.

- Strings and a single character are the same type of object in
  Python, but not in C++. Overall, make sure you understand each data
  type well first. Start with simple data types before you go into
  containers.

- Many basic programming constructs are similar: variables, data
  types, operations, operator precedence, functions, loops, files,
  etc. You will find that for loops generally involve a single integer
  counter, no range function. Learn the basic syntax for these first.

- Containers will be different. Instead of lists in Python that can be
  used for everything, you will need to learn about arrays, lists and
  vectors in C++. All containers we used had flexible length, while in
  C++, some will have predefined size. 

- You will see classes in C++ are very similar, but have a few new
  limitations like private attributes that can only be used within the
  class. This is actually a good thing, believe me.

For more in depth description of the differences see:

   http://cs.slu.edu/~goldwasser/publications/python2cpp.pdf

   http://www4.wittenberg.edu/academics/mathcomp/shelburne/comp255/notes/Python2Cpp.pdf

Setting up your C++ Working Environment
----------------------------------------

Your basic development environment in C++ consists of an editor for
writing programs, a Terminal window for compiling and running your
programs and a C++ compiler that you must install.

Here are the `detailed install instructions <setting_up_for_ds.html>`_.

-  You must have a C++ compiler installed.

-  You must have a terminal to run the compiler on. The terminal
   replaces the "Python Shell" version of Wing for you.

-  You must use an editor to write your programs. This replaces the
   editor portion of Wing. Many choices exist. The choice of editor is
   not so important, but becoming proficient in using an editor is.

As most of the installation will generally involve getting familiar
with an editor, here are some common terminal operations below.

   
Basic Terminal Operations
-------------------------

Basic terminal operations (Terminal in Macs and Cygwin in PCs) include:

-  Displaying the current working directory the terminal is pointing
   to::

    $ pwd


-  Listing the files in the current working directory for the
   terminal::

     $ ls
     $ ls p*   ##lists files that start with p
     $ ls Dropbox   ## lists files in the directory Dropbox 
                  ## (assuming it is one level below it)

-  Changing the working directory to a directory on your file system
   (cd means change directory)::

     $ cd directory_name
     $ cd directory1/directory2   ## if you want to change multiple
                                ## levels of directory in a single step
     $ cd ..  ## goes one level up in the dictionary hierarchy

-  Compile code::

     $ g++ programname -o outputname 


   For example::

     $ g++ program.cc -o program

   This generates a new file called `program` in Macs and `program.exe`
   in PCs. 

-  To run a program called `program`, use::

     $ ./program

-  Create a symbolic link (a shortcut) between two folders is very good
   way to simplify your life. Suppose you are at your own Desktop. I
   will create a shortcut to a directory on my dropbox on my own
   Desktop::

     $ pwd
     /Users/sibeladali/Desktop
     $ ln -s /Users/sibeladali/Dropbox/CSCI1100_Fall2014/ cs1
    
  This tells me to create a symbolic link (`ln -s`) for
  directory `/Users/sibeladali/Dropbox/CSCI1100_Fall2014/` and call
  it `cs1`. Now, I can simply write the following::

     $ cd cs1


You are now ready to install your C++ setup.

Here are the `detailed install instructions <setting_up_for_ds.html>`_.
