"""
This is a program to calculate the surface area and
volume of a cylinder given a radius and a height.

Radius and height are in float and are user inputs.

Sample Execution:
Enter radius (float) => 12
12
Enter height (float) => 10
10
Surface area is: 1658.76
Volume is: 4523.89

Course: CS1
Author(s): Wesley Turner, Konstantin Kuzmin
Date: 9/18/2017, modified 1/28/2019
"""


import math

def area_circle(radius):
    """
    This function returns the area of a circle with a given radius.

    Input parameters:
    radius (float) - the radius of the circle

    Return value:
    A float value of the area of the circle
    """

    area = math.pi * radius ** 2
    return area

def area_cylinder(h, r):
    """
    Give a height h and radius r, return the surface area of a cylinder.
    
    Input parameters:
    r (float) - the radius of the base of the cylinder
    h (float) - the height of the cylinder

    Return value:
    A float value of the surface area of the cylinder
    """

    cap_area = 2 * area_circle(r)
    rect_area = math.pi * 2 * r * h
    return cap_area + rect_area

if __name__ == "__main__":
    r = input("Enter radius (float) => ")
    print(r)
    r = float(r)
    h = input("Enter height (float) => ")
    print(h)
    h = float(h)
    print("Surface area is: {:.2f}".format(area_cylinder(h, r)))
    print("Volume is: {:.2f}".format(h * area_circle(r)))
