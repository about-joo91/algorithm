from collections import deque
import sys

sys.stdin = open('', 'r')
N = int(input())

graph = [input() for _ in range(N)]
r_g_weekness_visited = [[0] * N for _ in range(N)]
group_visited = [[0] * N for _ in range(N)]
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def get_r_g_weakeness_group(row, column):
    r_g_queue = deque()
    r_g_queue.append((row, column))
    cur_color = graph[row][column]
    while r_g_queue:
        cur_row, cur_col = r_g_queue.popleft()
        
        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]
            
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                    continue
            
            if r_g_weekness_visited[next_row][next_col]: continue
            
            if (cur_color == "R" or cur_color == "G") and\
            (graph[next_row][next_col] == "R" or graph[next_row][next_col] == "G"):
                r_g_weekness_visited[next_row][next_col] = 1
                r_g_queue.append((next_row, next_col))

            elif cur_color == graph[next_row][next_col]:
                 r_g_weekness_visited[next_row][next_col] = 1
                 r_g_queue.append((next_row, next_col))
    return True

def get_group(row, column):
    queue = deque()
    queue.append((row, column))
    cur_color = graph[row][column]
    while queue:
        cur_row, cur_col = queue.popleft()
        
        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]
            
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
                    continue
            
            if group_visited[next_row][next_col]: continue
            
            if cur_color == graph[next_row][next_col]:
                group_visited[next_row][next_col] = 1
                queue.append((next_row, next_col))
    return True


r_g_cnt = 0
cnt = 0
for i in range(N):
    for j in range(N):
        if not group_visited[i][j] and get_group(i, j):
            cnt+=1
        if not r_g_weekness_visited[i][j] and get_r_g_weakeness_group(i, j):
            r_g_cnt+=1

print(f"{cnt} {r_g_cnt}")

