"""
Quick code snippet to demonstrate walking through a list operating on 
all pairs of list elements without repeating matches and without operating
on the diagonals.

CS1
"""

L = [2, 21, 12, 8, 5, 31]
i = 0

dist = abs(L[0] - L[1])
indices = 0, 1

while i < len(L):
    j = i + 1
    while j < len(L):
        test_dist = abs(L[i] - L[j])
        if test_dist <= dist:
            dist = test_dist
            indices = i, j
        j += 1
    i += 1

print("Closest {} at {}.".format(dist, indices))