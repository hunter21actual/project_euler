from math import sqrt

def is_prime(n):
    lim = int(sqrt(n))
    cnt = 2
    for i in range(2, lim + 1):
        if(n % i == 0):
            cnt = cnt + 1
    if(cnt == 2):
        return True
    else:
        return False

pp = 1
np = -1
cnt = 1
tt = 5
i = 2
jj = 0
while(pp > 0.1):
    flag = 0
    while(flag != 4):
        if(is_prime(cnt) == True):
            np = np + 1
        cnt = cnt + i
        flag = flag + 1
    i = i + 2
    pp = np / tt
    tt = tt + 4

tt = tt - 4
print((tt+1)/2)
