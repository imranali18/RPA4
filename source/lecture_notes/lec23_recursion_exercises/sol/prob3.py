
def fib(n):
    if n==0 or n==1:
        return n
    m2 = 0
    m1 = 1
    for i in range(2,n+1):
        m = m1 + m2
        m2 = m1
        m1 = m
    return(m)


if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
