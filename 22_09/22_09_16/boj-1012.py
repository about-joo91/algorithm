import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(graph, visited, r, c, row, col):
    if 0 <= r < row and 0 <= c < col and visited[r][c] == 0 and graph[r][c] == 1:
        visited[r][c] = 1
        dfs(graph, visited, r + 1, c, row, col)
        dfs(graph, visited, r - 1, c, row, col)
        dfs(graph, visited, r, c + 1, row, col)
        dfs(graph, visited, r, c - 1, row, col)
        return True
    return False

T = int(input())

for _ in range(T):
    col, row, loc_cnt = map(int, input().split())
    graph = [[0] * col for _ in range(row)]
    visited = [[0] * col for _ in range(row)]
    for _ in range(loc_cnt):
        c, r = map(int, input().split())
        graph[r][c] = 1
    
    cnt = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 1 and visited[i][j] == 0:
                if dfs(graph, visited, i, j, row, col): cnt+=1
    print(cnt)