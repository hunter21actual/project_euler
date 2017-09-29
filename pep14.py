'''a = []

for n in range(1,1000000):
    c = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            c = c + 1
        else:
            n = 3 * n + 1
            c = c + 1
    a.append(c)

print(a.index(max(a)) + 1)'''


a = 1000000
high = 0

while (a > 10000):
    c = 0
    while a > 1:
        if a % 2 == 0:
            a = a // 2
            c = c + 1
        else:
            a = 3 * a + 1
            c = c + 1
    if(c > high):
        high = c
    a = a - 1

print(a,high)
