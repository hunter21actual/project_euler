def sieve(n):
    s = list(range(n + 1)) 
    s[1] = 0
    for i in range(2, int(n**0.5) + 1): 
        if s[i]:
            s[i*i: n + 1: i] = [0] * len(range(i*i, n + 1, i))
    return filter(None, s)

pr = list(sieve(7081))


num = []
for i in range(len(pr)):
    for j in range(len(pr)):
        for k in range(len(pr)):
            m = pr[i]**2 + pr[j]**3 + pr[k]**4
            if m < 50000000:
                num.append(m)
            else:
                break

print("Bless you boys")
print(len(set(num)))
