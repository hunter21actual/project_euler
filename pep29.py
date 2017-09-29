k=[]
a=int(input())
b=int(input())
for i in range(2,a+1):
    for j in range(2,b+1):
        m=i**j
        k.append(m)
k.sort()
new=set(k)
ton=list(new)
ton.sort()
print(len(ton))
