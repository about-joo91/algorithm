dp = [0] * 5001

N = int(input())

dp[3] = dp[5] = 1

for i in range(6, N+1):
    if dp[i - 3]: dp[i] = dp[i-3]+1
    if dp[i - 5]:
        dp[i] =  min(dp[i], dp[i-5]+1) if dp[i] else dp[i-5]+1
if dp[N] == 0:
    print(-1)
else:
    print(dp[N])