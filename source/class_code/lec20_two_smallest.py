import random
import time

def index_two_v1(values):
    if len(values) == 0:
        return
    if len(values) == 1:
        return 0, 0
    if values[0] > values[1]:
        least = 1
        next_least = 0
    else:
        least = 0
        next_least = 1
    for index in range(2, len(values)):
        if values[index] < values[least]:
            next_least = least
            least = index
        elif values[index] < values[next_least]:
            next_least = index
    return least, next_least
            


def index_two_v2(values):
    """
    Store the values in a list of value,index pairs and sort, then
    return the indices associated with the first two values
    """

    pairs = []
    for i in range(len(values)):
        pairs.append((values[i], i))
    pairs.sort()
    return pairs[0][1], pairs[1][1]   # indices of the values are in location 1 of each pair



if __name__ == "__main__":
    n = int(input("Enter the number of values to test ==> "))
    values = list(range(0, n))
    random.shuffle(values)

    s1 = time.time()
    (i0, i1) = index_two_v1(values)
    t1 = time.time() - s1
    print("Ver 1:  indices ({},{}); time {:.3f} seconds".format(i0, i1, t1))

    s2 = time.time()
    (j0, j1) = index_two_v2(values)
    t2 = time.time() - s2
    print("Ver 2:  indices ({},{}); time {:.3f} seconds".format(j0, j1, t2))
