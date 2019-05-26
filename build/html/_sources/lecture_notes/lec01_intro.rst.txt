Lecture 1 — Introduction
=========================================================


What is RPA?
-----------

-  RPA is an acronym for Robotic Process Automation

-  Robotic Process Automation is the technology that allows anyone today to configure computer software, or a “robot”
   to emulate and integrate the actions of a human interacting within digital systems to 
   execute a business process. RPA robots utilize the user interface to capture data and manipulate 
   applications just like humans do. They interpret, trigger responses and communicate with other systems 
   in order to perform on a vast variety of repetitive tasks. Only substantially better: an RPA software robot never sleeps, makes zero mistakes and costs a lot less than an employee.


How does Robotic Process Automation Work ? 
------------------------------------------

-  RPA robots are capable of mimicking many–if not most–human user actions. They log into applications, move files and folders, 
   copy and paste data,  fill in forms, extract structured and semi-structured data from documents, scrape browsers, and more.


What are the Business Benefits of RPA ?
---------------------------------------

- Robots are here to stay. The faster you harvest their potential, the faster you create a competitive edge for your business.
  Robotic Process Automation delivers direct profitability while improving accuracy across organizations and industries. Enabling RPA to handle any processes will not only transform and streamline your organization’s workflow. It will allow for superior scalability and flexibility within the enterprise, doubled by fast, tailored response to specific needs. Software robots are easy to train and they integrate seamlessly into any system. Multiply them, and instantly deploy more as you go. They constantly report on their progress so you can go even bigger and better by using operational and business predictability, while improving strategically.
  
  - Better Accuracy: Robotic Process Automation software robots are programmed to follow rules. 
    They never get tired and never make mistakes. They are compliant and consistent.
  - Improved Compliance: Once instructed, RPA robots execute reliably, reducing risk. Everything they do is monitored. 
    You have the full control to operate in accordance with existing regulations and standards.
  - Fast Cost Savings: RPA can reduce processing costs by up to 80%. In less than 12 months, most enterprises already 
    have a positive return on investment, and potential further accumulative cost reductions can reach 20% in time.
  - Super Scalable: Across business units and geographies, RPA performs a massive amount of operations in parallel, 
    from desktop to cloud environments. Additional robots can be deployed quickly with minimal costs, according to work flux and seasonality.
  - Increased Speed and Productivity: Employees are the first to appreciate the benefits of RPA as it removes non-value-add 
    activities and relieves them from the rising pressure of work       

.. image:: RPA1.jpg



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


