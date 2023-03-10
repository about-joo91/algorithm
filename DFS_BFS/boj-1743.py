import sys
from collections import deque
input = sys.stdin.readline

def get_size_of_waste(start_row, start_col):
    queue = deque()
    queue.append((start_row, start_col))
    visited[start_row][start_col] = True
    size = 1

    while queue:
        cur_row, cur_col= queue.popleft()

        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]

            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M: continue
            if visited[next_row][next_col]: continue
            if hotel_map[next_row][next_col] == 0: continue

            visited[next_row][next_col] = True
            queue.append((next_row, next_col))
            size+=1

    return size

N, M, K = map(int, input().split())
hotel_map = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
for _ in range(K):
    row, col = map(int, input().split())
    hotel_map[row-1][col-1] = 1

answer = 0
for i in range(N):
    for j in range(M):
        if visited[i][j]: continue
        if hotel_map[i][j] == 0: continue
        answer= max(answer, get_size_of_waste(i, j))

print(answer)