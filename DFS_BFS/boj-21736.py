from collections import deque

N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
start = (0, 0)
for i in range(N):
    for j in range(M):
        if graph[i][j] == 'I':
            start = (i, j)

def count_meeting_people(row, col):
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True
    count = 0
    while queue:
        cur_row, cur_col = queue.popleft()
        if graph[cur_row][cur_col] == 'P': count+=1
        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]
            if next_row < 0 or next_row >= N or next_col < 0 or next_col >=M: continue
            if visited[next_row][next_col]: continue
            if graph[next_row][next_col] == 'X': continue
            
            visited[next_row][next_col] = True
            queue.append((next_row, next_col))
    return count

meeting_count = count_meeting_people(*start)
print(meeting_count if meeting_count else 'TT')