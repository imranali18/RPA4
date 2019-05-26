Lecture 1 — Introduction
=========================================================

People
------

-  Instructor: Konstantin Kuzmin

-  Humanities Focused Section: James Malazita

-  Instructional Support Coordinator: Erica Eberwein

-  TAs and programming mentors:  see course Website

Learning Outcomes
-----------------

#. Demonstrate proficiency in the purpose and behavior of basic
   programming constructs.

#. Design algorithms and programs to solve small-scale computational
   programs.

#. Write, test and debug small-scale programs

#. Demonstrate an understanding of the widespread application of
   computational thinking to real-world problems.

Textbook
--------

-  *Practical Programming: An Introduction to Computer Science Using
   Python* by Campbell, Gries, and Montojo

   -  Available in e-book form

-  We will be using **second edition** but if you have third edition, it should also be fine.


Website and Online Resources
-----------------------------

-  Course notes and lecture exercises will be posted at:

       http://www.cs.rpi.edu/academics/courses/spring19/csci1100

-  Submitty will be used for posting homework assignments and labs, and as a
   public discussion site:

       https://submitty.cs.rpi.edu/index.php?semester=s19&course=csci1100&component=forum&page=view_thread
       
   You will be automatically added when you enroll. Let an instructor or TA know if you cannot log into this site more than **48 hours** after you receive notice from the registrar that you are enrolled. The site is updated daily, not immediately, so there might be some lag.


Other items from the syllabus
-----------------------------

-  Dr. Kuzmin's office hours are:

   -  Tues 4:00 pm - 5:30 pm and Thurs 11:30 am - 1:00 pm, both in AE112

-  Other office hours are posted online

-  Lab sections are held Tuesdays and Wednesdays. Full credit will be given for 
   finishing the lab within your lab period. Checkpoints completed before your 
   next lab will receive half credit.

   -  **Important exception:** For the last checkpoint only... If you show up on time and work through the entire lab period, we will give you full credit for a **final** checkpoint that is completed before your next lab.


-  Requirements and grading: lecture exercises, labs, homework assignments, tests; letter grades

-  Appealing grades

-  Class attendance and participation; lecture notes

-  Homework late policy:

   - 6 LATE DAYS FOR THE WHOLE SEMESTER
   - 2 LATE DAYS ON ANY ONE ASSIGNMENT

-  Academic integrity

-  Other exceptions: report to me right now or as soon as you know

-  Notes on schedule:

   -  Labs start next week. As of the end of that lab (Lab 0) you should
      have all the pieces you need to successfully complete 
      the remaining labs and homework assignments for the semester. If you have problems 
      completing Lab 0, please get help. You have to get it done to proceed and you really need to be 
      finished before Lab 1.

   -  No labs during the weeks of February 17 (President's Day), March 3 (Spring break), and March 24 (GM week).

   -  Test dates are February 7, March 14, and April 11, all from 6:15 pm to 7:45 pm (90 minutes). You must be here or have an excused absence from Student Experience. If you do not have an excused absence for a test, you will get a 0. **No exceptions**!

   -  Final exam will be held during finals week.  **No exceptions**!  So,
      don't make departure plans until the final exam schedule is posted.


The Magic of Programming
------------------------

-  Cold, harsh logic, and

-  Seemingly primitive syntax...

-  Leading to soaring creativity!

Types of Problems We Will Study
-------------------------------

-  Tools used to help you win at *Words with Friends*

-  Image processing and manipulation

-  Web searching and crawling

-  Programs that work with data from Yelp

-  Numerical examples, including games and physical simulations

-  Perhaps even a simple version of (part of) Pokemon Go.

Jumping In Quickly with Our First Program — Hello World
-------------------------------------------------------

-  We create a text file called ``hello.py`` containing just the two lines of Python code:

   ::

         print('Hello, World!')
         print('This is Python')

-  This is done by launching the Wing IDE, which is specific to creating
   and running Python programs

   -  IDE stands for ’Integrated Development Environment’

         -  Two windows will appear — the top being the editor and the bottom
            being the Python interpreter

-  Load the ``hello.py`` program

-  Run it using the interpreter

-  We can also type Python code directly into the interpreter.



Something a Bit More Interesting
--------------------------------

-  We are going to emphasize computational thinking throughout the
   semester, so let’s look at a fun little problem and get started.

-  This problem is posed in *Think Python* and taken from the NPR show
   *Car Talk*. If you know the answer, do NOT say it!

       "Find the one word in the English language that contains three
       consecutive double letters."

-  We will talk through the steps needed to develop and test a Python
   program to solve this problem.

   -  The file containing this program will be posted on the course
      website after class.

-  We do **not** intend that you will understand the details of the
   program at this time. Rather, this is just an exercise that
   illustrates the steps of solving a fun problem computationally.

-  On the other hand, it does introduce some elements that will be
   seeing repeatedly throughout the semester:

   -  Files

   -  Functions

   -  Loops

   -  Logic

   -  Counting

   -  Output

   -  Libraries

-  In about six weeks, you will understand all parts of this program!

-  You can see the code in :mod:`three_doubles` from :doc:`../class_code`

Looking Back: What Steps Did We Follow?
---------------------------------------

#. Developing an understanding of what the problem is really asking.
   This usually involves playing around with small examples.

#. Developing and describing a recipe (an “algorithm”) for solving the
   problem

   -  Most recipes will involve multiple parts — multiple functional
      steps

#. Turning this recipe into a program in the formal language of Python,
   one of many different programming languages.

   -  English is too imprecise for specification of programs.

#. Running this program using the Python interpreter.

Programs, Compilers, Interpreters, Abstractions
-----------------------------------------------

-  Python is an interpreted language — run immediately and interactively
   by the Python interpreter, which is itself another (very complex)
   program

-  Programs in some other (non-interpreted) languages like C, C++ and
   Java must be compiled (by a “compiler” — another program) into a new
   program in machine assembly language and then executed.

-  In both cases, we write programs that require other programs to run.

   -  And, we don’t just need just the compiler or interpreter — we need
      the file system, the operating system, and the command-line
      interpreter, each of them complicated, multi-part programs
      themselves.

-  We don’t really think about the details of these programs; we just
   think of what they do for us.

   -  This is called an “abstraction”.

   -  It allows us to think about a problem we are trying to solve
      without thinking about all the details of all the other systems we
      are depending on.

   -  Thinking in terms of abstractions is fundamental to computer
      science.

Why Python?
-----------

-  Python has a very simple syntax

   -  The roles of indentation and blank lines cause the most confusion.

-  Interpreted languages provide immediate, useful feedback

-  Python has a powerful set of tools — abstractions

-  Python is widely used in science, engineering, and industry.

-  Python is good for rapid prototyping

   - Sometimes, after a Python program is written and working, the
     most time-consuming steps are rewritten in either C or C++ and
     then integrated with the Python code.

Two Types of Errors in Our Python Programs
------------------------------------------

-  A *syntax error* is a mistake in the form of the Python code that
   will not allow it to run.

-  A *semantic error* is a mistake in the “meaning” of the program,
   causing it to produce incorrect output, even if it runs.

-  We will demonstrate both types of errors by deliberately introducing
   errors in our triple double example program.

Python Versions
---------------

-  Python, like all programming languages, is continually under
   development.

-  We will be using the latest version installed by the *conda* package.

Lab 0 — Tuesday and Wednesday next week!
----------------------------------------

By the end of Lab 0, you should have:

#. Visited the Submitty site and browsed the forum and file repositories

      https://submitty.cs.rpi.edu/index.php?semester=s19&course=csci1100

#. Gone to the course page

      http://www.cs.rpi.edu/academics/courses/spring19/csci1100/python_environment.html

   and followed the instructions to install the Python environment on
   your computer.

   -  There are installers for “native” versions of the environment for
      Windows, Mac OS X, and Linux machines. 

#. Created a Dropbox account to store back-up copies “in the cloud” of
   homework and lab solutions and lab for the course.

   -  Other cloud-based back-up copies are acceptable.

   -  This is required. Do not come to us the day your homework is due and tell us you lost your data! Dropbox gives you a **private** cloud backup and version control. 

   -  I love *github* and *gitlab*. **Do not use them for your coursework**. We take academic integrity seriously in this course. If you publish your code online and someone copies it, you are responsible. 

