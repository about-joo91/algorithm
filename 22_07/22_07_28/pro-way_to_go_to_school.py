def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    puddles = [[y, x] for x,y in puddles]

    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == j == 1:
                dp[i][j] = 1
                continue
            if [i, j] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] +dp[i][j-1])%1000000007
    return dp[n][m]

print(solution(4,3,[[2, 2]]))