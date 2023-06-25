N = int(input())

dp = [0] * (N+1)
dp[0] = 1

for i in range(1, N+1):
    cur_num = 0
    for j in range(i):
        cur_num += (dp[i-j-1] * dp[j])
    dp[i] = cur_num

print(dp[N])
