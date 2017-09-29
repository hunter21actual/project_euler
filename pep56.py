k = []
ss = []

for i in range(2, 100):
    for j in range(2, 100):
        m = i**j
        k.append(m)
k.sort()

ton = list(set(k))
ton.sort()

maxx = 0
for i in range(len(ton)):
    summ = 0
    n = ton[i]
    while (n > 0):
        r = n % 10
        summ = summ + r
        n = n // 10
    if (summ > maxx):
        maxx = summ
print(maxx)    
        
