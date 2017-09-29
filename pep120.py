def rmax(a):
    arr = []
    arr.append(((a+1)**2+(a-1)**2)%(a*a))
    arr.append((2*a)%(a*a))
    i = 3
    pat = -10
    while(pat != arr[1]):
        pat = ((a+1)**i+(a-1)**i)%(a*a) 
        arr.append(pat)
        i = i + 2
    return max(arr)

ans = 0
for i in range(3, 1001):
    ans = ans + rmax(i)
print(ans)


