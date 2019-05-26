def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
def fib_non(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        l = n*[0]
        l[1] = 1
        for i in range(2, n+1):
            l[i] = l[i-1] + l[i-2]
            print(l)
        return l[n]

for i in range(11):
    print("{}: {}", format(i, fib(i)))