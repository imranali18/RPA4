from math import sqrt
"""
This module contains a simple example of a Point2d class developed
during lecture
"""


class Point2d(object):
    """
    Implement a point class 
    """
    def __init__(self, x0=0, y0=0):
        """
        Initialization
        """
        self.x = x0
        self.y = y0
        
    def __add__(self, other):
        """
        Add two points
        """
        return Point2d(self.x + other.x, self.y + other.y)
        
    def magnitude(self):
        """
        Distance from the origin
        """
        return sqrt(self.x**2 + self.y**2)

    def dist(self, o):
        """
        Distance between 2 points
        """
        return sqrt((self.x - o.x)**2 + (self.y - o.y)**2)
    
if __name__ == "__main__":
    p = Point2d(0, 4)
    q = Point2d(5, 10)
    Point2d.__add__(p, q)
    leng = Point2d.magnitude(q)
    print("Magnitude {:.2f}".format(leng))
    print("Distance is {:.2f}".format(Point2d.dist(p, q)))
