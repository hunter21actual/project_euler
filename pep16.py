n = int(input())
p = 2**n
print(p)
s = 0
while p>0:
    m = p % 10
    s = s + m
    p = p // 10
print(s)    
    
