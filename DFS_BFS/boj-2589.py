from collections import deque
N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

def bfs(start):
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    while queue:
        cur_row, cur_col, cur_dist = queue.popleft()

        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]

            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M: continue
            if visited[next_row][next_col]: continue
            if graph[next_row][next_col] == "W": continue

            visited[next_row][next_col] = True
            queue.append((next_row, next_col, cur_dist+1))

    return cur_dist


answer = 0
for i in range(N):
    for j in range(M):
        if graph[i][j] == "L":
            answer = max(answer, bfs((i, j, 0)))

print(answer)