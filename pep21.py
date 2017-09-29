a=[]
b=[]
d=[]
e=[]
f=[]

for i in range(1,10001):
    a.append(i)

for i in range(len(a)):
    c=[]
    for j in range(1,int(a[i]/2)+1):
        if a[i]%j==0:
            c.append(j)
    b.append(sum(c))

for i in range(len(a)):
    d.append((a[i],b[i]))

for i in range(len(a)):
    for j in range(len(a)):
        if d[i][0]==d[j][1] and d[i][1]==d[j][0] and d[i][0]!=d[i][1]:
            e.append(d[i])

for i in range(len(e)):
    f.append(e[i][0])

print(sum(f))
