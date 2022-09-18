# 파이썬 통과 코드
import sys

N = int(input())

if int(N **(1/2)) == N ** 0.5:
    print(1)
    sys.exit(0)

for i in range(1, int(N**0.5)+1):
    if int((N - i**2) ** 0.5) == (N- i**2) ** 0.5:
        print(2)
        sys.exit(0)

for i in range(1, int(N**0.5)+1):
    for j in range(1, int((N - i**2) **0.5)+1):
        if int((N - i**2 - j**2) ** 0.5) == (N- i**2 - j**2)**0.5:
            print(3)
            sys.exit(0)
print(4)

# pypy 통과 코드
import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N+1)
dp[0] = 0
dp[1] = 1
for i in range(2, N+1):
    min_value = 4
    j = 1
    while ((j**2) <= i):
        min_value = min(min_value, dp[i- j**2])
        j+=1
    dp[i] = min_value +1
print(dp[N])