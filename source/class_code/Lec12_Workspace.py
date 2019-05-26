"""
Calculate the distance between two (x, y) coordinates. This is used
later in the closest points calculation
"""


def dist(x, y):
    return ((x[0] - y[0])**2 + (x[1] - y[1])**2)**0.5

"""
Two loops to demonstrate manipulation of
loop variables for "for" and "while" loops.
"""

n = int(input("N?: "))

print("For:")
for i in range(2, n, 2):
    print(i)
    
print("\nWhile:")
i = 2
while i < n:
    print(i)
    i += 2

