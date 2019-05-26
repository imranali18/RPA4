"""
Two implementations of the closest point calculation, one using
an auxiliary list and one not using an auxiliary list.
"""


def distance(p1, p2):
    """
    Calculate the distance between two points.
    """
    return ((p1[1] - p2[1])**2 + (p1[0] - p2[0])**2)**0.5

def closest_points_1(points):
    """
    Calculate the closest distance between two points using a distance array
    """

    dist = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist.append([distance(points[i], points[j]), i, j])
    return min(dist)

def closest_points_2(points):
    """
    Calculate the closest distance between two points without using a distance array
    """

    small = distance(points[0], points[1])
    i1 = 0
    i2 = 1
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = distance(points[i], points[j]) 
            if dist < small:
                small = dist
                i1 = i
                i2 = j
    return small, i1, i2

points = [(1, 5), (13.5, 9), (10, 5), (8, 2), (16,3)]

cp = closest_points_1(points)
print("Closest dist of {:.2f} occurs between {} and {}".format(cp[0], points[cp[1]], points[cp[2]]))
cp = closest_points_2(points)
print("Closest dist of {:.2f} occurs between {} and {}".format(cp[0], points[cp[1]], points[cp[2]]))
