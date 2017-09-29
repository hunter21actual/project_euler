from itertools import permutations
perms = [int(''.join(p)) for p in permutations(['1','2','3','4','5','6','7','8','9'])]

a = []
for i in range(9000,10000):
    a.append(int(str(i)+str(2*i)))

print(max(set(a).intersection(set(perms))))  



