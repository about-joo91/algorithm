N, K = map(int, input().split())

dp = [0] * (N + 1)
dp[0] = 1

for _ in range(1, K+1):
    for i in range(1, N+1):
        print(dp)
        dp[i] = (dp[i] + dp[i-1])% 1000000000
print(dp[N])