import random
def ins_sort(L):
    for i in range(1,len(L)):
        j = i - 1
        x = L[i]
        while x < L[j] and j >= 0:
            L[j+1] = L[j]
            j -= 1
        L[j+1] = x
        
            

if __name__ == "__main__":
    L = list(range(10))
    print(L)
    random.shuffle(L)
    print(L)
    
    ins_sort(L)
    print(L)
    