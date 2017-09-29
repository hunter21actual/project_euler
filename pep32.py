arr = []

for i in range(100, 1000):
    for j in range(10,100):
        mul = (i*j)
        prod = str(i)+str(j)+str(mul)
        if(''.join(sorted(prod)) == '123456789'):
            arr.append(i*j)

for i in range(1000, 10000):
    for j in range(1,10):
        mul = (i*j)
        prod = str(i)+str(j)+str(mul)
        if(''.join(sorted(prod)) == '123456789'):
            arr.append(i*j)

print(sum(set(arr)))
