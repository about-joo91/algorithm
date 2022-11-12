from collections import deque
import sys

sys.stdin = open('', 'r')

N , M = map(int, input().split())

map_of_maze = [list(map(int,list(input()))) for _ in range(N)]
distances = [[[-1] * 2 for _ in range(M)] for _ in range(N)]

directions = [[0, 1], [1, 0] , [-1, 0] , [0, -1]]
queue = deque()

queue.append((0, 0, 1))
distances[0][0][0] = distances[0][0][1] = 1

while queue:
    cur_row, cur_col, is_not_broken = queue.popleft()
    
    if cur_row == N-1 and cur_col == M-1:
        print(distances[cur_row][cur_col][is_not_broken])
        break
    
    for direction in directions:
        next_row = cur_row + direction[0]
        next_col = cur_col + direction[1]

        next_distance = distances[cur_row][cur_col][is_not_broken] +1
        if 0 <= next_row < N and 0 <= next_col < M and distances[next_row][next_col][is_not_broken] == -1:
            if map_of_maze[next_row][next_col] == 0 :
                distances[next_row][next_col][is_not_broken] = next_distance
                queue.append((next_row, next_col, is_not_broken))
                
            if is_not_broken and map_of_maze[next_row][next_col] == 1:
                queue.append((next_row, next_col, 0))
                distances[next_row][next_col][0] = next_distance
                
else: print(-1)
