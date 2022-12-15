import sys
from collections import defaultdict
input = sys.stdin.readline

R, C = map(int, input().split())
maps = [ list(input()) for _ in range(R)]
visited = [[False] *C for _ in range(R)]
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]


used = defaultdict(str)
answer = 0

def dfs(row, col):
    global answer
    answer = max(answer, len(used))

    for direction in directions:
        next_row = row + direction[0]
        next_col = col + direction[1]
        if 0 > next_row or next_row >= R or 0 > next_col or next_col >= C: continue
        if visited[next_row][next_col]: continue

        if maps[next_row][next_col] not in used:
            used[maps[next_row][next_col]]
            dfs(next_row, next_col)
            del used[maps[next_row][next_col]]

visited[0][0] = True
used[maps[0][0]] = 1
dfs(0, 0)
print(answer)