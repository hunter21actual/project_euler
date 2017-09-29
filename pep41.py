#Valuable insight: find sum of an n digit pandigital nos. All except 4-pan and 7-pan are divisible by 3 and hence cannot be prime
#Therefore when considering 'n'-pandigital nos only 4-pan and 7-pan can be primes

n=int(input())

ans=[]

def pan(n):
    a=str(n)
    b=[]
    c=[]
    for i in range(len(a)):
        b.append(int(a[i]))
    big=max(b)
    for i in range(1,big+1):
        c.append(i)
    b.sort()
    c.sort()
    if b==c:
        return True
    else:
        return False

def sieve(n):
    np = n + 1
    s = list(range(np)) 
    s[1] = 0
    sqrtn = int(n**0.5)
    for i in range(2, sqrtn + 1): 
        if s[i]:
            s[i*i: np: i] = [0] * len(range(i*i, np, i))
    return filter(None, s)

pp=list(sieve(n))

for i in range(len(pp)):
    if pan(pp[i])==True:
        ans.append(pp[i])

print(max(ans))
