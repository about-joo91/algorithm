while True:
    cur_num = int(input())
    if cur_num == 0: break

    dp = [[0] * (cur_num+1) for _ in range(cur_num+1)]
    
    for i in range(cur_num+1):
        dp[0][i] = 1
    
    for i in range(1, cur_num+1):
        for j in range(i, cur_num+1):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
            
    print(dp[cur_num][cur_num])