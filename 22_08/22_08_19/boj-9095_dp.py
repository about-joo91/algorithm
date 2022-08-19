import sys
T = int(sys.stdin.readline())
dp = [0] * 11
dp[1] = 1
dp[2] = 2
dp[3] = 4
for _ in range(T):
    cur_num = int(sys.stdin.readline())
    for i in range(4, cur_num+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]
    print(dp[cur_num])