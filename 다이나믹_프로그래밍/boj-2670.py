N = int(input())
decimals = [float(input()) for _ in range(N)]
dp = [-1] * N
dp[0] = decimals[0]

for i in range(1, N):
    dp[i] = max(decimals[i], dp[i-1] * decimals[i])

print("{:.3f}".format(max(dp)))