import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    dp = [list(range(0, n+1)) for _ in range(k+1)]
    for i in range(1, k+1):
        for j in range(1, n+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    print(dp[k][n])