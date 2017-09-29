i = 10
def f(n):
    if(''.join(sorted(str(n))) == ''.join(sorted(str(2*n))) and ''.join(sorted(str(n))) == ''.join(sorted(str(3*n))) and ''.join(sorted(str(n))) == ''.join(sorted(str(4*n))) and ''.join(sorted(str(n))) == ''.join(sorted(str(5*n))) and ''.join(sorted(str(n))) == ''.join(sorted(str(6*n))) ):
        return True

while (f(i) != True):
    i = i + 1
    
print(i)
