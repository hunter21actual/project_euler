A=[]
maxx = 0
for i in range(100, 1000):
    for j in range(100, i):
        k = i * j
        g = str(k)
        p = int(g[::-1])
        if p == k and p > maxx:
            maxx = p
        

print(maxx)            
    
            
