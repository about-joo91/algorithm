N = int(input())
houses = [list(map(int, input().split())) for _ in range(N)]
INF = int(10e6)
answer = INF
for i in range(3):
    dp = [[INF]* 3 for _ in range(N+1)]
    dp[1][i] = houses[0][i]
    for j in range(2, N+1):
        dp[j][0] = houses[j-1][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = houses[j-1][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = houses[j-1][2] + min(dp[j-1][0], dp[j-1][1])
    dp[N][i] = INF
    answer = min(answer, min(dp[N]))

print(answer)