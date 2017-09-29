from math import *
print("Bless you boys")

def sieve(n):
    s = list(range(n + 1)) 
    s[1] = 0
    for i in range(2, int(n**0.5) + 1): 
        if s[i]:
            s[i*i: n + 1: i] = [0] * len(range(i*i, n + 1, i))
    return filter(None, s)

p1 = list(sieve(3340))
p2 = list(sieve(1000))
pp = list(set(p1) - set(p2))
pp.sort()

def ispr(n):
    c = 0
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            c = c + 1
    if c == 0:
        return True
    else:
        return False

num = []

for i in range(len(pp)):
    r1, r2, r3 = pp[i], pp[i] + 3330, pp[i] + 6660
    a, b, c = set(str(r1)), set(str(r2)), set(str(r3))
    if ispr(r2) == True and ispr(r3) == True and a == b and b == c:
        num.append([r1,r2,r3])
                
for i in range(len(num)):
    print(str(num[i][0]) + str(num[i][1]) + str(num[i][2]))

