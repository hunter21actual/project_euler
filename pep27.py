from math import *

def sieve(n):
    s = list(range(n + 1)) 
    s[1] = 0
    for i in range(2, int(n**0.5) + 1): 
        if s[i]:
            s[i*i: n + 1: i] = [0] * len(range(i*i, n + 1, i))
    return filter(None, s)

def isprime(n):
    if n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    c = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            c = c + 1
    if c == 0:
        return 1
    else:
        return 0

bb = list(sieve(1000))

b = []

for i in range(len(bb)):
    b.append(-1*bb[i])
    b.append(bb[i])

b.sort()

maxx, a1, b1 = 0, 0, 0

for a in range(-999, 1000, 2):
    for j in range(len(b)):
        n, c = 0, 0
        while (isprime(abs(n**2 + a*n + b[j])) != 0):
            if isprime(abs(n**2 + a*n + b[j])) == 1:
                c = c + 1
            n = n + 1

        if c > maxx:
            maxx = c
            a1 = a
            b1 = b[j]

print(a1*b1)
