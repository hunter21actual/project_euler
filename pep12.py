n=100000

import timeit

start = timeit.default_timer()

tnos=[]

def t(n):
    return int((n*(n+1))/2)

for i in range(1,n+1):
    tnos.append(t(i))

def sieve(n):
        s = list(range(n + 1)) 
        s[1] = 0
        for i in range(2, int(n**0.5) + 1): 
            if s[i]:
                s[i*i: n + 1: i] = [0] * len(range(i*i, n + 1, i))
        return filter(None, s)
    
def nod(n):

    a = []
    b = []

    k = list(sieve(int(n**0.5) + 2))

    for i in range(len(k)):
            if n % k[i] == 0:
                    a.append(k[i])

    for i in range(len(a)):
            j = 1
            while n % (a[i]**j) == 0: 
                    j = j + 1
            b.append(j - 1)

    nod = 1

    for i in range(len(b)):
            nod = nod * (b[i] + 1)

    return nod

for i in range(len(tnos)):
    if nod(tnos[i]) >= 500:
        print(tnos[i])
        break
            
stop = timeit.default_timer()

print(stop - start) 

