from itertools import permutations
sperms=[]
perms = [''.join(p) for p in permutations(['0','1','2','3','4','5','6','7','8','9'])]
for i in range(len(perms)):
    m=int(perms[i])
    sperms.append(m)
sperms.sort()
print(sperms[999999])


