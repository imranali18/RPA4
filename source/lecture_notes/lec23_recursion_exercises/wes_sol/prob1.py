
def recursive_add_impl(L, level):
    if level == len(L) - 1:
        return L[level]
    return L[level] + recursive_add_impl(L, level+1)
        

def recursive_add(L):
    if len(L) == 0:
        return 0

    return recursive_add_impl(L, 0)

if __name__ == "__main__":
    L1 = [ 5 ]
    print(recursive_add(L1))
    L2 = [ 24, 23.1, 12, 15, 1 ]
    print(recursive_add(L2))
    print(recursive_add([ ]))
