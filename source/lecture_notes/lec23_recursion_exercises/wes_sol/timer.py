import time
import prob2
import prob3

def timer(f, n):
    start = time.time()
    val = f(n)
    end = time.time()
    return end - start

if __name__ == "__main__":
    for i in range(1,6):
        print("Iterative Fibonacci: {}: {:.6f}".format(10*i, timer(prob3.fib, 10*i)), flush=True)
        print("Recursive Fibonacci: {}: {:.6f}".format(10*i, timer(prob2.fib, 10*i)), flush=True)
        print()