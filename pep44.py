n=int(input())
def p(n):
    return (n*(3*n-1))/2
def absolute(x):
    if x<0:
        return -x
    else:
        return x
for i in range(1,n+1):
    for j in range(1,i+1):
        c=p(i)+p(j)
        d=absolute(p(i)-p(j))
        if ((24*c+1)**0.5+1)%6==0 and ((24*d+1)**0.5+1)%6==0:
            print(c)
            print(d)
            print('pentagonal')

            
