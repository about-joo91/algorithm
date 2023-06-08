N = int(input())
health_points = list(map(int, input().split()))
joy_points = list(map(int, input().split()))

dp = [[0] * 100 for _ in range(N+1)]

for i in range(1, N+1):
	for j in range(1, 100):
		cur_health = health_points[i-1]
		cur_joy = joy_points[i-1]
		if cur_health <= j:
			dp[i][j] = max(dp[i-1][j], dp[i-1][j-cur_health] + cur_joy)
		else:
			dp[i][j] = dp[i-1][j]

print(dp[N][-1])
