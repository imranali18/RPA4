
def fib(n):
    L = [0, 1]
    if n < 2:
        return L[n]
    for i in range(2, n+1):
        L.append(L[i-1] + L[i-2])

    return L[n]

if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
