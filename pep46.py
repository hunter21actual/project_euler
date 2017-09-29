n=int(input())

aa=[]

for i in range(1,n+1,2):
    aa.append(i)

def sieve(n):
    np = n + 1
    s = list(range(np)) 
    s[1] = 0
    sqrtn = int(n**0.5)
    for i in range(2, sqrtn + 1): 
        if s[i]:
            s[i*i: np: i] = [0] * len(range(i*i, np, i))
    return filter(None, s)

kk=list(sieve(n))

def gold(n):
    k=list(sieve(n))
    m=[]
    for i in range(1,int(n**0.5)):
        m.append(i)
    for i in  range(len(k)):
        for j in range(len(m)):
            if n==k[i]+2*(m[j]**2):
                return True

cc=list(set(aa)-set(kk))

for i in range(1,len(cc)):
    if gold(cc[i])!=True:
        print(cc[i])
        break
        




