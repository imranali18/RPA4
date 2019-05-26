"""
Building the list of legos from a file. Each line of this file 
contains the name of a lego and the number of copies of that 
lego, separated by a comma.  For example,
2x1, 3
2x2, 2
"""


lego_name = input('Enter the name of the legos file: ').strip()
lego_list = []
for line in open(lego_name):
    line = line.split(',')
    lego = line[0].strip()   # get rid of extra space
    count = int(line[1])
    # Either of the following two lines work...
    # lego_list.extend([lego] * count)
    lego_list = lego_list + [lego] * count
print(lego_list)
