import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
answer = 0

def update_answer_to_max_value(depth, row, col, cur_sum):
    global answer
    if depth == 3:
        answer = max(answer, cur_sum)
        return
    
    for direction in directions:
        next_row = row + direction[0]
        next_col = col + direction[1]
        
        if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M: continue
        
        if visited[next_row][next_col]: continue

        if depth == 1:
            visited[next_row][next_col] = True
            update_answer_to_max_value(depth+1, row, col, cur_sum + graph[next_row][next_col])
            visited[next_row][next_col] = False

        visited[next_row][next_col] = True
        update_answer_to_max_value(depth+1, next_row, next_col, cur_sum +graph[next_row][next_col])
        visited[next_row][next_col] = False

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        update_answer_to_max_value(0, i, j, graph[i][j])
        visited[i][j] = False
print(answer)