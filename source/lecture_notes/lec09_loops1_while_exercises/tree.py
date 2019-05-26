'''
n = int(input("Enter the height of the tree: "))

i = 1
while i <= n:
    print( ' '*(n-i) + '*'*(2*i-1) )
    i += 1

base_line = ' '*(n-2) + '***'
print(base_line)
print(base_line)
'''

"""
width = int(input("Enter the (odd) width of the tree: "))

i = 1
while i <= width:
    print( ' '*((width-i)//2) + '*'*i )
    i += 2

base_line = ' '*(width//2-1) + '***'
print(base_line)
print(base_line)
"""

i = 1
while i <= 9:
    print( ' ' * ((9-i)//2) + '*'*i )
    i += 2

base_line = ' '*3 + '*'*3
print(base_line)
print(base_line)
