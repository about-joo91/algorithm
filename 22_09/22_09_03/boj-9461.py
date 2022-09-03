test_case = int(input())
dp = [0] * 101
dp[1] = 1
dp[2] = 1
dp[3] = 1
for _ in range(test_case):
    cur_num = int(input())
    for i in range(4, cur_num+1):
        dp[i] = dp[i-2] + dp[i-3]
    print(dp[cur_num])