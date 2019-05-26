Lecture 13 --- Exercises
========================

Solutions to the problems below must be sent to Submitty for grading.
A separate file must be submitted for each problem. Solutions must be
submitted by 09:59:59 am on Friday, March 1.

#. Given the file ``census_data.txt``:

   ::

       Line 1 |Location    2000    2011
       Line 2 |New York State  18,976,811  19,378,102
       Line 3 |New York City   8,008,686   8,175,133
       Line 4 |

   What is the output of the following code? (Note: the line
   numbers and the "|" are not actually in the file, they are just there to show 
   that the contents is 4 lines.)

   ::

       f = open("census_data.txt")
       line1 = f.readline()
       line1 = line1.strip()
       line2 = f.read()
       line3 = f.readline()
       print(line1)
       print(line2)
       print(line3)
       f.close()
       f = open("census_data.txt")
       s = f.read()
       line_list = s.split('\n')  
       print(len(line_list))
       line_list = s.strip().split('\n')
       print(len(line_list))

   Submit your output as a text file.

#. Given a file containing test scores, one per line, we want to have
   a new file that contains the scores in increasing order. To do
   this, write a Python program that asks the user for two file name
   strings, one for the input scores and the second for the output,
   sorted scores. The program should open the first file (to read),
   read the scores, sort them, open the second file (to write), and
   output to this file the scores in increasing order. There should be
   one score per line, with the index on each line.

   As an example, suppose the input file is ``scores.txt`` and it
   contains:

   ::

      75
      98
      75
      100
      21
      66
      83
      15

   then running your program should look like (in Wing IDE 101):

   ::

      Enter the scores file: scores.txt
      scores.txt
      Enter the output file: scores_sorted.txt
      scores_sorted.txt

   When you look at the contents of ``scores_sorted.txt`` you should
   see:

   ::

      0:  15
      1:  21
      2:  66
      3:  75
      4:  75
      5:  83
      6:  98
      7: 100

   (Output the indices using two integer spaces {:2d} and the scores using
   three integer spaces {:3d}.) You only need to submit the Python file. We will test with the
   example above and with a new file you have not seen.
