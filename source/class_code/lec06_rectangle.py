"""
Program to demonstrate the use of complex boolean expressions and if/elif/else
clauses. Determine whether a set of coordinates fall within a rectangle given
by the vertices (x0, y0), (x0, y1), (x1, y1), and (x1, y0)

Author: CS1 Staff
Date 9/21/2017
"""

"""
Initialize the rectangle
"""
x0 = 10
x1 = 16
y0 = 32
y1 = 45

"""
Get the target point
"""
x = input("x coordinate ==> ")
print(x)
x = float(x)
y = input("y coordinate ==> ")
print(y)
y = float(y)

"""
If the x coordinate matches x0 or x1 and we are within the y range, we are
on the boundary. Similarly, if the y coordinate matches y0 or y1 and we are 
within the x range, we are also on the boundary
"""
if ((x == x0 or x == x1) and (y0 <= y <= y1) or (y == y0 or y == y1) and (x0 <= x <= x1)):
    print("Point ({:.2f},{:.2f}) is on the boundary.".format(x, y))
elif (x0 < x < x1) and (y0 < y < y1):
    """
    If we are not on the boundary, but we are in range in both x and y, 
    then we are inside the rectangle
    """
    print("Point ({:.2f},{:.2f}) is inside the rectangle.".format(x, y))
else:
    """
    If we are not on the boundary and we are not inside the rectangle, then
    we must be inside.
    """
    print("Point ({:.2f},{:.2f}) is outside the rectangle.".format(x, y))
