def squarefree(n):
    pri = [4,9,25,49]
    cnt = 0
    for i in range(len(pri)):
        if( n % (pri[i]) == 0):
            cnt = cnt + 1
    if(cnt != 0):
        return False
    else:
        return True

n = 50
arr = []
c = [[0 for x in range(n+1)] for y in range(n+1)]

for i in range(0, n+1):
    for j in range(0, n+1):
        if(j == 0 or i == j):
            c[i][j] = 1
        else:
            c[i][j] = 0;
            
            
for i in range(1, n+1):
    for j in range(0, i+1):
        if(i != j):
            c[i][j] = c[i-1][j-1] + c[i-1][j]
            
for i in range(1, n+1):
    for j in range(0, i+1):
        arr.append(c[i][j])

new = list(set(arr))

ans = 0
for i in range(len(new)):
    if(squarefree(new[i]) == True):
        ans = ans + new[i]

print(ans)
