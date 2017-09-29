def f(m,n):
    return m*n*(m+1)*(n+1)/4

for i in range(2,1000):
    for j in range(2,i):
        if(f(i,j) > 1999995 and f(i,j) < 2000005):
            print(i, j)

