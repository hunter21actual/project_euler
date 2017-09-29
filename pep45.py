n=int(input())
a=[]
b=[]
c=[]

def tri(n):
    return int((n*(n+1))/2)

def penta(n):
    return int((n*(3*n-1))/2)

def hexa(n):
    return int(n*(2*n-1))

for i in range(1,n+1):
    a.append(tri(i))
    b.append(penta(i))
    c.append(hexa(i))

u=set.intersection(set(a),set(b),set(c))    
print(u)

