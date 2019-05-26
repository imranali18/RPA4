class yrange:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            i = self.i
            self.i += 1
            return i
        else:
            raise StopIteration()

def zrange(n):
    i = 0
    while i<n:
        yield i
        i += 1

class list_gen:
    def __init__(self, v):
        self.v = v
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < len(self.v):
            self.i += 1
            return self.v[ self.i-1 ]
        else:
            raise StopIteration()

def list_gen_f(v):
    i = 0
    while i<len(v):
        yield v[i]
        i += 1

for x in yrange(10):
    print(x)
print('-'*10)
for x in zrange(10):
    print(x)
print('-'*10)
for x in list_gen( ['a', 'b', 'c', 'd' ] ):
    print(x)
print('-'*10)
for x in list_gen_f( ['a', 'b', 'c', 'd' ] ):
    print(x)

