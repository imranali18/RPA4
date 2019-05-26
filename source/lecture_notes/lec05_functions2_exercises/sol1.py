def area_rect(width, length):
    return width*length

def area_solid(width, length, height):
    return 2*area_rect(width,length) + 2*area_rect(width,height) + 2*area_rec(length,height)

def middle_three( x0, x1, x2 ):
    return x0 + x1 + x2 - min(x0,x1,x2) - max(x0,x1,x2)

def test_middle( x0, x1, x2):
    print ('middle of ({0:d},{1:d},{2:d}) is {3:d}'.format(x0,x1,x2,
                                                          middle_three(x0,x1,x2)))

test_middle( 0, 10, 20 ) 
test_middle( 30, 10, 20 )
test_middle( 30, 25, 30 )
