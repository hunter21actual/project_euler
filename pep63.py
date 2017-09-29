n = int(input())
a = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        k = i ** j
        if len(str(k)) == j:
            a.append(k)
a.sort()
print(len(a))
