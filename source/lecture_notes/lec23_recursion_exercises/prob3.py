
def fib(n):
    f = [0, 1]
    if n < 2:
        return f[n]
    else:
        for i in range(2, n+1):
            f.append(f[i-1] + f[i-2])
    return f[n]    

if __name__ == "__main__":
    print( fib(0) )
    print( fib(1) )
    print( fib(2) )
    print( fib(5) )
    print( fib(10) )
