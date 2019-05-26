"""
Here is a short example to show the calculation of a mode
when there is and is not an "enumerable" mapping between 
values and indices. (For the not enumerable, assume the values
are floats or sparsely distributed.

We assume scores are hockey scores. They cannot be negative.
"""

scores = [(3, 2), (2, 1), (9, 1), (8, 7), (2, 0), (0,4), (1,7), (29, 6), (27, 29), (30, 29), (2, 29)]

"""
Assume the values have an efficient mapping to indices of a list
"""

"""
Find the range for the enumeration.
"""
high = scores[0][0]
for score in scores:
    if score[0] > high:
        high = score[0]
    if score[1] > high:
        high = score[1]

"""
Now generate a list of occurrence values and increment when you see a value occur.
"""
L = (high + 1) * [0]
for score in scores:
    L[score[0]] += 1
    L[score[1]] += 1
    
"""
Report the enumerable case.
"""
most = max(L)
print("Max occurrence: {}".format(most))
if most == 1:
    print("No Mode")
else:
    for index in range(len(L)):
        if L[index] == most:
            print("Mode is at: {}".format(index))
            
"""
------------------------------------------------------
Now do it again assuming the values are not enumerable
------------------------------------------------------
"""

"""
Make a single list in sorted order
"""
L = []
for score in scores:
    L.append(score[0])
    L.append(score[1])
L.sort()

"""
Walk through the list looking for where the breaks in the sorted list
occur and use that to count occurences
"""
curr = 0   # Count value, current max
index = 0  
prev = -1  # Element value from previous grouping
count = 0
modes = [] # All the values that have the maximum
while index < len(L):
    if L[index] != prev:
        if count > curr:
            modes = [prev]
            curr = count
        elif count == curr:
            modes.append(prev)
        prev = L[index]
        count = 1
    else:
        count += 1
    index += 1
    
if count > curr:
    modes = [prev]
    curr = count
elif count == curr:
    modes.append(prev)
print(modes)

