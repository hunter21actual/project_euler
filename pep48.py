n=int(input())
s=0
for i in range(1,n+1):
    s=s+i**i
print(s)
m=s

k=0
for j in range(0,10):
    r=m%10
    k=k+r*10**j
    m=m//10
print(k)
