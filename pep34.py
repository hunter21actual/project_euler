n=int(input())
c=0
d=0
for i in range(2,n+1):
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        d=d+i
print(d)            
