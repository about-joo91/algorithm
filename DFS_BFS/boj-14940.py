from collections import deque

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
queue = deque()
for i in range(N):
    for j in range(M):
        if graph[i][j] == 2:
            queue.append((i, j))
            break;

while queue:
    cur_row, cur_col = queue.popleft()
    for d_row, d_col in directions:
        next_row = cur_row + d_row
        next_col = cur_col + d_col

        if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M:
            continue
        if graph[next_row][next_col] != 1:
            continue

        graph[next_row][next_col] += graph[cur_row][cur_col]
        queue.append((next_row, next_col))

for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            continue

        graph[i][j] -=2

for i in range(N):
    print(" ".join(list(map(str, graph[i]))))
