N, S, M = map(int, input().split())

volumes = [0] + list(map(int, input().split()))

dp = [[ ] for _ in range(N +1) ]

dp[0] = [S]

for i in range(1, N+1):
    for j in range(len(dp[i-1])):
        plus_volume = dp[i-1][j] + volumes[i]
        minus_volume = dp[i-1][j] - volumes[i]

        if 0 <= plus_volume <= M and plus_volume not in dp[i]:
            dp[i].append(plus_volume)
        if 0 <= minus_volume <= M and minus_volume not in dp[i]:
            dp[i].append(minus_volume)
if dp[N]:
    print(max(dp[N]))
else: print(-1)