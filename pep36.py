a = []

for i in range(1,1000001):
    k = str(i)
    m2 = k[::-1]
    s = bin(i)
    m = s[2:]
    m1 = m[::-1]
    if k == m2 and m == m1:
        a.append(i)

print(sum(a))
