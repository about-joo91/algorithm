import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

R, C = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(R)]
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
dp = [[-1] * C for _ in range(R)]


def dfs(r, c):
    if r == R -1 and c == C -1:
        return 1
    
    if dp[r][c] != -1:
        return dp[r][c]
    
    dp[r][c] = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and maps[r][c] - maps[nr][nc]> 0:
            dp[r][c] += dfs(nr, nc)
    return dp[r][c]
print(dfs(0,0))