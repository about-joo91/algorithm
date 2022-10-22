import sys

sys.setrecursionlimit(2000)

def get_minimum_path(cur_row, cur_col, cur_pos):
    if cur_row == n:
        return 0

    if dp[cur_row][cur_col][cur_pos] != INF:
        return dp[cur_row][cur_col][cur_pos]

    for next_pos, direction in enumerate(directions):
        next_row, next_col = cur_row + 1, cur_col + direction
        
        if cur_pos != next_pos and 0<= next_col < m:
            
            data = get_minimum_path(next_row, next_col, next_pos) + maps[cur_row][cur_col]
            dp[cur_row][cur_col][cur_pos] = min(data, dp[cur_row][cur_col][cur_pos])

    return dp[cur_row][cur_col][cur_pos]

INF = int(1e9)
n, m = map(int, input().split())
answer = INF
dp = [[[INF] * 3 for i in range(m)] for _ in range(n)]
directions = [-1, 0, 1]
maps = [list(map(int, input().split())) for _ in range(n)]

for i in range(m):
    for j in range(3):
        answer = min(answer, get_minimum_path(0, i, j))

print(answer)