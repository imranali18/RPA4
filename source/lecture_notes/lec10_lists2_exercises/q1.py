L1 = [ 1, 5, [5,2], 'hello' ]
L2 = L1
L3 = L1.copy()
L2.append( 4 )
L1.append( 3 )

print(L1[0], L1[-1], len(L1))
print(L3[0], L3[-1], len(L3))
