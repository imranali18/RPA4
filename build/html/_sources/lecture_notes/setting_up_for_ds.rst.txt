Setting up C++ for Data Structures
=====================================

This material is compiled with the help of many mentors over the
years. Special thanks to Micheal Gardner and Lee Cattarin for their
edits on prior versions of this document.

Remember to leave install fest with the following tools and skills:

- A compiler that works
- Ability to compile and run a program on the terminal

It is also a good idea to have an editor or an IDE that works. If you
have additional time, install an editor and ask a mentor or TA to show
you how to use it. But this is less important. Below are instructions
on possible ways to accomplish this.


Installing a terminal and a compiler
------------------------------------

Data Structures requires that your C++ code compile and run on the
``gcc/g++ 4.8.x`` compiler. You may also use ``clang++``, which
provides more concise and clear error messages. How you install a
compiler will depend on your operating system, which requires the
compiler program and a Terminal to run it on.

- If you have *Windows 10*, you will likely want to install
  Windows Subsystem for Linux (WSL). Detailed instructions to install
  this can be found on the Data Structures course website:

  https://www.cs.rpi.edu/academics/courses/fall18/csci1200/development_environment.php 
  
-- in particular:
  
  https://www.cs.rpi.edu/academics/courses/fall18/csci1200/wsl.php 
  
  should walk through most if not all of the relevant steps.

-  If you have **Windows 7 or 8** WSL is not available and your best
   option is installing ``Cygwin``. Detailed instructions to install this
   can be found on the Data Structures course website:

   http://www.cs.rpi.edu/academics/courses/fall17/csci1200/cygwin.php
   
  **BUT** it is not necessary to go through "Helpful edits to the
  Cygwin ``.bashrc`` file" right now.

-  If you have a **Mac**, you'll need **XCode**, which provides both a
   compiler and an IDE for you.

   For Data Structures, **make sure to install XCode's "Command
   Line Tools"** so that you can compile and run your code in the
   terminal as well as the IDE. Install instructions for XCode and
   XCode Command Line Tools can be found:
   
   http://railsapps.github.io/xcode-command-line-tools.html

   You can then run a Terminal window: Terminal under
   Applications->Utilities in Macs (black box)
   
-  If you have a Linux OS such as **Ubuntu**, installing is easy. Run
   the following three commands in a terminal window:
  
   ::
      
       sudo apt-get install g++
       sudo apt-get install clang++-3.8
       sudo apt-get install gcc-multilib g++-multilib

Choosing an editor or IDE (Integrated Development Environment)
---------------------------------------------------------------

A text editor will allow you to view and edit your code (often with
syntax highlighting or other features), but not compile and run - you
have to do that in a terminal (cygwin, for Windows). An IDE will do
all of these things, but might take more time to learn how to navigate
as they are usually fuller-featured. Whichever you choose, **you will
still have to learn how to compile and run your code in a terminal**,
as that is the primary method to get help or show completeness in lab.

-  If you want a text editor, these options are popular:

   - Sublime Text: http://www.sublimetext.com/
   - Atom (very similar to Sublime Text): https://atom.io/
   - Notepad++: https://notepad-plus-plus.org/
     Windows only, note that this is **not** Notepad
   - Gedit: https://wiki.gnome.org/Apps/Gedit\#Download
     (this is usually installed by default on some Linux systems)
   - There are also terminal editors like

     Vim: http://www.vim.org/
     
     Nano: https://www.nano-editor.org/
     
     Emacs: https://www.gnu.org/software/emacs/
     
     but these may have a steeper learning curve!


-  If you want an IDE, these options work with the compiler you'll be
   using:

   - Eclipse: http://www.eclipse.org/cdt/
     (this is used in a later Computer Science course as well)
   - Code::Blocks: http://www.codeblocks.org/
   - Xcode (Mac only): https://developer.apple.com/xcode/
   - NetBeans: https://netbeans.org/features/cpp/

     and from the Data Structures site, notes on using NetBeans with C and C++:

     http://chriseiffel.com/uncategorized/windows-c-compiler-how-to/

If you are having trouble deciding, ask the TAs and mentors what they use!

Remember: IDEs are useful for debugging with a graphical user
interface. But, it is likely that no one will be an expert in the
specific IDE you use. Practice and learn its features before starting
to use it in class assignments.


Final Note
----------

If you find additional resources that are useful, please feel free to
let us know. We will include them here.


