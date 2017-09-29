def is_inc(n):
    inc = -1
    up = 0
    while(n > 0):
        if(n % 10 > inc):
            up = up + 1
        inc = n%10
        n = n // 10

    if(len(str(n)) == up):
        return True
    else:
        return False
            
def is_dec(n):
    r = int(str(n)[::-1])
    dec = -1
    down = 0
    while(r > 0):
        if(r % 10 > dec):
            down = down + 1
        dec = r%10
        r = r // 10

    if(len(str(r)) == down):
        return True
    else:
        return False

def is_bouncy(n):
    if(is_inc(n) == False and is_dec(n) == False):
        return True
    else:
        return False

ans = 0
i = 100
p = 0
while(p != 0.99):
    if(is_bouncy(i) == True):
        ans = ans + 1
    p = ans/i
    i = i + 1

print(i-1)
