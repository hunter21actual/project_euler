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

def sieve(n):
    s = list(range(n + 1)) 
    s[1] = 0
    for i in range(2, int(n**0.5) + 1): 
        if s[i]:
            s[i*i: n + 1: i] = [0] * len(range(i*i, n + 1, i))
    return filter(None, s)

p = list(sieve(1000000))
cp = []

for i in range(len(p)):
    m = len(str(p[i]))
    m1 = m

    n1 = p[i]
    n2 = p[i]
    l = 1
    while(m1 - 1 != 0):
        n1 = n1 // 10
        n2 = n2 % (10**(m1 - 1))
        m1 = m1 - 1
        if isprime(n1) == 1 and isprime(n2) == 1:
            l = l + 2
    
    if l == (2*m - 1) and p[i] > 10:
        cp.append(p[i])

    if len(cp) == 11:
        print(sum(cp))
        break
    

