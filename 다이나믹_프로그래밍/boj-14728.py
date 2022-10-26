N, K = map(int, input().split())

dp = [[0] * (K+1) for _ in range(N+1)]

times = []
scores = []

for _ in range(N):
    time, score = map(int, input().split())
    times.append(time)
    scores.append(score)
    
for i in range(1, N+1):
    for current_time in range(1, K+1):
        if times[i-1] <= current_time:
            dp[i][current_time] = max(dp[i-1][current_time], scores[i-1] + dp[i-1][current_time- times[i-1]])
        else: dp[i][current_time] = dp[i-1][current_time]
print(dp[N][K])