"""
Demonstrate importing and using a 'homegrown' module. In this file
we are importing the Lec11_module code. Note that the code in the

if __name__ == "__main__":

block is not executed, but we can read in and use the "addto" function.
"""


import lec11_module

print(lec11_module.addto(5, 7))