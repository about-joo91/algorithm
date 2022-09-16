import sys
from math import factorial

input = sys.stdin.readline
N= int(input())
numbers = str(factorial(N))
i = -1

while numbers:
    if numbers[i] != "0":
        break
    i-=1
    
        
print(-i-1)