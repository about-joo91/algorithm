from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

for _ in range(T):
    M, N = map(int, input().split())
    maze = [input() for _ in range(N)]
    
    visited = [[0] * M for _ in range(N)]
    
    route_queue = deque()
    
    for i in range(N):
        for j in range(M):
            if maze[i][j] == "*":
                route_queue.append((i,j, "*"))
                visited[i][j] = 1
                
    for i in range(N):
        for j in range(M):
            if maze[i][j] == "@":
                route_queue.append((i,j, "@"))
                visited[i][j] = 1
                
    while route_queue:
        
        cur_row, cur_col, type_ = route_queue.popleft()
        
        if type_ == "@" and (cur_row == 0 or cur_row == N-1 or cur_col == 0 or cur_col == M-1):
            print(visited[cur_row][cur_col])
            break
        
        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]
            
            if 0 > next_row or next_row >= N or 0 > next_col or next_col >= M: continue 
            if visited[next_row][next_col]: continue
            if maze[next_row][next_col] == "#": continue
            
            visited[next_row][next_col] = visited[cur_row][cur_col] + 1
            route_queue.append((next_row, next_col, type_))
    else: print("IMPOSSIBLE")