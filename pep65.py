def f(n):
    add = 0
    while(n > 0):
        add = add + (n%10)
        n = n//10
    return add

a = []
a.append(2)
a.append(1)
a.append(2)
j = 1
k = 4
while(len(a) < 10000):
    if(j % 3 == 0):
        a.append(k)
        k = k + 2
    else:
        a.append(1)
    j = j + 1


i = len(a) - 1
den = a[i]
num = 1
bb = 0 
while(i != 0):
    temp = den
    num = a[i-1]*den + num
    den = num
    num = temp
    i = i - 1

print(f(den))




