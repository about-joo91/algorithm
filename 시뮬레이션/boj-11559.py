from collections import deque
import sys
input = sys.stdin.readline

graph = [list(input()) for _ in range(12)]
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]



def check_same_color(color_type, row, col):
    queue = deque()
    queue.append((row, col))
    visited[row][col]= 1
    cnt = 1
    while queue:
        cur_row, cur_col = queue.popleft()
        tmp.append((cur_row, cur_col))

        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]

            if 0<= next_row < 12 and 0 <= next_col < 6 and not visited[next_row][next_col] and graph[next_row][next_col] == color_type:
                visited[next_row][next_col] = 1
                queue.append((next_row, next_col))
                cnt+=1
                    
    return cnt

cnt = 0
while True:
    visited = [[0] * 6 for _ in range(12)]
    answers = []
    for i in range(12):
        for j in range(6):
            tmp = []
            if not visited[i][j] and graph[i][j] != ".":
                if check_same_color(graph[i][j], i, j) >= 4:
                    for row, col in tmp:
                        graph[row][col] = "."
                    answers+= tmp
    if len(answers) == 0:
        break
    cnt+=1
    for answer in answers:
        cur_row, cur_col = answer[0], answer[1]

        next_row = cur_row -1
        
        while next_row >= 0 and graph[next_row][cur_col] == ".":
            next_row-=1
        if next_row < 0: continue

        while next_row >= 0:
            graph[next_row][cur_col], graph[cur_row][cur_col] = graph[cur_row][cur_col], graph[next_row][cur_col]
            next_row-=1
            cur_row-=1
    


print(cnt)