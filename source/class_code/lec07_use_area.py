"""
Lecture 7 - Demonstrate the use of the area calculations
Prof. Charles Stewart
"""

import lec07_area

r = 6
h = 10
a1 = lec07_area.circle(r)
a2 = lec07_area.cylinder(r, h)
a3 = lec07_area.sphere(r)
print("Area circle {:.1f}".format(a1))
print("Surface area cylinder {:.1f}".format(a2))
print("Surface area sphere {:.1f}".format(a3))
