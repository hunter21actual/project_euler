n = int(input())

a = [n**2]

def grid(n):
    k = n - 1
    m = n**2
    c = 0
    while k > 1:
        m = m - k
        c = c + 1
        if c % 4 == 0:
            k = k - 2
        a.append(m)

grid(n)

print(sum(a))
