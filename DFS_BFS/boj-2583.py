from collections import deque
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

graph = [[0] * M  for _ in range(N)]
visited = [[0] * M for _ in range(N)]
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for _ in range(K):
    c1, r1, c2, r2 = map(int, input().split())
    
    for i in range(r1,r2):
        for j in range(c1, c2):
            if graph[i][j] == 1: continue
            graph[i][j] = 1
            
def get_white_area(row:int, column:int) -> int:
    
    queue = deque()
    queue.append((row, column))
    visited[row][column] = 1
    area = 1
    
    while queue:
        cur_row, cur_col = queue.popleft()
        
        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]
            
            if next_row < 0 or next_row >= N or next_col <0 or next_col >=M: continue
            if visited[next_row][next_col]: continue
            if graph[next_row][next_col] == 1:continue
            
            visited[next_row][next_col] = 1
            queue.append((next_row, next_col))
            area +=1
    return area


answer = []
            
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0 and not visited[i][j]:
            answer.append(get_white_area(i, j))

print(len(answer))            
print(*sorted(answer))