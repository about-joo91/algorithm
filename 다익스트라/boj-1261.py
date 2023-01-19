import sys
from collections import deque
input = sys.stdin.readline
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def get_minimum_cnt_of_broken_wall():

    queue = deque()
    queue.append((0, 0))
    dist[0][0] = 0
    while queue:
        cur_row, cur_col = queue.popleft()

        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]
            
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M: continue
            if dist[next_row][next_col] != -1: continue
            
            if maps[next_row][next_col] == 0:
                dist[next_row][next_col] = dist[cur_row][cur_col]
                queue.appendleft((next_row, next_col))
            else:
                dist[next_row][next_col] = dist[cur_row][cur_col] + 1
                queue.append((next_row, next_col))

    return dist[N-1][M-1]
    

M, N = map(int, input().rstrip().split())
maps = [list(map(int, list(input().rstrip()))) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
print(get_minimum_cnt_of_broken_wall())
