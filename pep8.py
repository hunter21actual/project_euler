n=input()

a=[]
b=[]

for i in range(0,len(n)-12):
    k=int(n[i:i+13])
    a.append(k)
for i in range(0,len(a)):
    p = 1
    ele = b[i]
    while ele>0:
        r = ele%10
        p = p * r
        ele = ele // 10
    new = p
    b.append(new)

print(max(b))
