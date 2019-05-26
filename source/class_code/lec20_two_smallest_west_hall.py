import random
import time

def index_two_v1(values):
    # O(N)
    if values[1] < values[0]: # O(1)
        lowest = values[1]
        low = values[0]
        index_lowest = 1
        index_low = 0
    else:
        lowest = values[0]
        low = values[1]
        index_lowest = 0
        index_low = 1
    for i in range(2, len(values)): # N times the time of the inner part
        if values[i] < lowest:
            low = lowest
            index_low = index_lowest
            lowest = values[i]
            index_lowest = i
        elif values[i] < low:
            low = values[i]
            index_low = i
    return index_lowest, index_low



def index_two_v2( values ):
    # Generate a dictionary with values as keys and
    # a list of indices as values
    val_dict = dict()
    for index in range(len(values)): # O(N)
        if not values[index] in val_dict:
            val_dict[values[index]] = []
        val_dict[values[index]].append(index)
    
    # sort the keys
    sorted_keys = sorted(val_dict) #O(N log N)
    
    # pick out the indices of the smallest keys
    if len(val_dict[sorted_keys[0]]) > 1:
        return val_dict[sorted_keys[0]][0], val_dict[sorted_keys[0]][1]
    else:
        return val_dict[sorted_keys[0]][0], val_dict[sorted_keys[1]][0]

if __name__ == "__main__":
    n = int(input("Enter the number of values to test ==> "))
    values = list(range(0, n))
    random.shuffle(values)

    s1 = time.time()
    (i0,i1) = index_two_v1(values)
    t1 = time.time() - s1
    print("Ver 1:  indices ({},{}); time {:.3f} seconds".format(i0, i1, t1))

    s2 = time.time()
    (j0,j1) = index_two_v2(values)
    t2 = time.time() - s2
    print("Ver 2:  indices ({},{}); time {:.3f} seconds".format(j0, j1, t2))
