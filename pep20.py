from math import *

n = int(input())
k = factorial(n)

s = 0

while k>0:
    r = k%10
    s = s + r
    k = k // 10

print(s)    
