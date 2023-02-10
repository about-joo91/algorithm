import sys
sys.stdin.readline
N, M = map(int, input().split())
graph = [list(map(int,list(input()))) for _ in range(N)]
dp = [[0] * (M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        if i == j == 0:
            dp[i][j] = graph[i][j]
        elif graph[i][j] == 0:
            dp[i][j] = 0
        else:
            dp[i][j] = min(dp[i-1][j-1], dp[i-1][j] , dp[i][j-1]) +1
        
answer = max(map(max, dp))
print(answer **2)