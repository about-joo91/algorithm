from collections import deque
import sys
input = sys.stdin.readline

N , M = map(int, input().split())
visited = [[0] * N for _ in range(M)]
tomato_box = [list(map(int, input().split())) for _ in range(M)]
queue = deque()
directions = [[0,1], [0,-1], [1,0], [-1,0]]

def bfs():
    day = 0
    while queue:
        cur_row, cur_col, day = queue.popleft()
        visited[cur_row][cur_col] = 1
        for direc in directions:
            next_row = cur_row + direc[0]
            next_col = cur_col + direc[1]
            if 0 <= next_row < M and 0<= next_col < N and visited[next_row][next_col] == 0:
                if tomato_box[next_row][next_col] == 0:
                    tomato_box[next_row][next_col] = 1
                    queue.append((next_row, next_col, day+1))
    return day
                
for i in range(M):
    for j in range(N):
        if tomato_box[i][j] == 1:
            queue.append((i, j, 0))


day = bfs()

for i in range(M):
    if 0 in tomato_box[i]:
        print(-1)
        break
else: print(day)