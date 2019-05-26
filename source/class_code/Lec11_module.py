"""
Demonstrate importing and using a 'homegrown' module. In this file
we are defining the Lec11_module code. Note that the code in the

if __name__ == "__main__":

block is executed when this file is run, but not when we import it 
into Lec11_main. Either way the "addto" function remains available.
"""


def addto(val, increment):
    return val + increment

if __name__ == "__main__":
    # Put the main body of the program below this line
    n = int(input("Enter a positive integer ==> "))
    total = 0
    i = 0
    print(i, n)
    while i < n:
        print(i, n)
        total = addto(total, i)
        i += 1
    print('Sum is', total)