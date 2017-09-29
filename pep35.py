def isprime(n):
    c = 0
    for i in range(2, int(n**0.5) + 2):
        if n % i == 0:
            c = c + 1
    if c == 0:
        return True
    else:
        return False

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
    k = m
    l = 0
    pp = p[i]
    while(k != 0):
        pp = (pp % 10)*(10**(m-1)) + (pp // 10) 
        if isprime(pp) == True:
            l = l + 1
        k = k - 1 
    if l == m:
        cp.append(pp)
   
print(len(cp) + 1)
