n=600851475143

def sieve(n):
    np = n + 1
    s = list(range(np)) 
    s[1] = 0
    for i in range(2, int(n**0.5) + 1): 
        if s[i]:
            s[i*i: np: i] = [0] * len(range(i*i, np, i))
    return filter(None, s)

A=list(sieve(int(n**0.5)))
b=[]
for i in range(len(A)):
    if n%A[i]==0:
        b.append(A[i])
    
print(max(b))
