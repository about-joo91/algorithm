N = int(input())
jump_numbers = [0] + list(map(int, input().split()))
INF = int(10e9)
dp = [INF] * (N+1)
dp[1] = 0

for i in range(1, N+1):
    for j in range(1, jump_numbers[i]+1):
        if i + j > N: continue
        dp[i+j] = min(dp[i] + 1, dp[i+j])

if dp[-1] == INF:
    print(-1)
else: print(dp[-1])