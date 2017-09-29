from itertools import permutations

perms = [''.join(p) for p in permutations(['0','1','2','3','4','5','6','7','8','9'])]

beta=[]

def k1(d):
    return int(d[1]+d[2]+d[3])%2
def k2(d):
    return int(d[2]+d[3]+d[4])%3
def k3(d):
    return int(d[3]+d[4]+d[5])%5
def k4(d):
    return int(d[4]+d[5]+d[6])%7
def k5(d):
    return int(d[5]+d[6]+d[7])%11
def k6(d):
    return int(d[6]+d[7]+d[8])%13
def k7(d):
    return int(d[7]+d[8]+d[9])%17

for i in range(len(perms)):
    if k1(perms[i])==0 and k2(perms[i])==0 and k3(perms[i])==0 and k4(perms[i])==0 and k5(perms[i])==0 and k6(perms[i])==0 and k7(perms[i])==0:
        beta.append(int(perms[i]))

print(sum(beta))





        

