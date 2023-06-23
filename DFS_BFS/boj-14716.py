import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
directions = [[0, 1], [1, 0], [-1, 0], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
visited = [[False] * M for _ in range(N)]
def check_if_word(s_row, s_col):
    queue = deque()
    queue.append((s_row, s_col))
    visited[s_row][s_col] = True

    while queue:
        cur_r, cur_c = queue.popleft()
        for direction in directions:
            next_r = cur_r + direction[0]
            next_c = cur_c + direction[1]

            if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M: continue
            if visited[next_r][next_c]: continue
            if graph[next_r][next_c] == 0: continue
            visited[next_r][next_c] = True
            queue.append((next_r, next_c))

answer = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]: continue
        if graph[i][j] == 0: continue
        check_if_word(i, j)
        answer +=1

print(answer)