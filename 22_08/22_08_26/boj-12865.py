import sys
input = sys.stdin.readline
N , K = map(int, input().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
values = []
weights = []
for _ in range(N):
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)
for i in range(N+1):
    for j in range(K+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif weights[i-1] <= j:
            dp[i][j] = max(values[i-1] + dp[i-1][j - weights[i-1]], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])