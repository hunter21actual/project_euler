abn=[]
ele=[]
nash=[]

def sieve(n):
    np = n + 1
    s = list(range(np)) 
    s[1] = 0
    sqrtn = int(n**0.5)
    for i in range(2, sqrtn + 1): 
        if s[i]:
            s[i*i: np: i] = [0] * len(range(i*i, np, i))
    return filter(None, s)

def sod(n):
    a=[1]
    for i in range(2,int(n/2)+1):
        if n%i==0:
            a.append(i)
    return sum(a)

for j in range(1,28124):
    if sod(j)>j:
        abn.append(j)
        
for i in range(len(abn)):
    for j in range(len(abn)):
        k=abn[i]+abn[j]
        if k<28124:
            ele.append(k)

hill=set(ele)

for i in range(1,28124):
    nash.append(i)

new=list(set(nash)-hill)

print(sum(new))
            

