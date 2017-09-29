i = 1
den = 2
num = 1
ans = 0
while(i != 1000):
    temp = den
    num = 2*den + num
    den = num
    num = temp
    if( len(str(num + den)) > len(str(den))):
        ans = ans + 1
    i = i + 1

print(ans)

