import time
from math import *

def coeff(i, j):
    return int(factorial(i) / (factorial(j) * factorial(i - j)))

tStart = time.time()

c = 0

for i in range(23, 101):
    for j in range(0, i + 1):
        if coeff(i, j) > 1000000:
            c = c + 1

print(c)
print("Run Time = " + str(time.time() - tStart))
        
    
