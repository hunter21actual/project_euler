n=int(input())
for i in range(1,n+1):
    s=0
    k=i
    while i>0:
        r=i%10
        s=s+(r**5)
        i=i//10
    if s==k:
        print(s)
        
