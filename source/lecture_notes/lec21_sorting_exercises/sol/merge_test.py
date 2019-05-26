from merge import *

if __name__ == "__main__":
    L1 = [ 1, 2, 3, 4 ]
    L2 = [ 1, 2, 3, 4 ]
    L = merge(L1,L2)
    print( "L1 {}, L2 {}, Merged {}".format( L1, L2, L ))

    L1 = [ 1, 2, 3, 4 ]
    L2 = [ 5, 6 ]
    L = merge(L1,L2)
    print( "L1 {}, L2 {}, Merged {}".format( L1, L2, L ))

    L1 = [ 44, 55, 66, 77 ]
    L2 = [ 1, 10, 44, 55 ]
    L = merge(L1,L2)
    print( "L1 {}, L2 {}, Merged {}".format( L1, L2, L ))
           
