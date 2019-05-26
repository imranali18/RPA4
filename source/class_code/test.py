'''
This is a program to calculate the surface area and
volume of a cylinder given a radius and a height.

Radius and height are in float and are user inputs.

Sample Execution:
Enter radius (float) => 12
Enter height (float) => 10
Surface area is: 1658.76
Volume is: 4523.89

CS1
Wesley Turner
9/18/2017
'''
import lec05_surface_and_area as lec05

print("Above the if in file test, name =", __name__)

if __name__ == "__main__":
    print("Within the if in file test, name =", __name__)
    print("Surface area is: {:.2f}".format(lec05.area_cylinder(10, 2)))
    print("Volume is: {:.2f}".format(2 * lec05.area_circle(2)))
