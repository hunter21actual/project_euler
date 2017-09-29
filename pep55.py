def pal(n):
    if(str(n) == str(n)[::-1]):
        return True
    else:
        return False

def lych(n):
    it = 0
    while(it < 50):
        n = n + int(str(n)[::-1])
        it = it + 1
        if(pal(n) == True):
            break
        
    if(it < 50):
        return False
    else:
        return True

ans = 0
for i in range(0, 10000):
    if(lych(i) == True):
        ans = ans + 1

print(ans)
