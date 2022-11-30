from collections import deque
import sys
input = sys.stdin.readline

graph = [list(input()) for _ in range(12)]
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]



def get_same_color_cnt(color_type:str, row:int, col:int) -> int:
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

def pull_down_above_puyo() -> None:
    for answer in answers:
        cur_row, cur_col = answer[0], answer[1]

        next_row = cur_row -1
        
        while next_row >= 0:
            if graph[next_row][cur_col] == ".": 
                next_row-=1
            else:
                graph[next_row][cur_col], graph[cur_row][cur_col] = graph[cur_row][cur_col], graph[next_row][cur_col]
                next_row-=1
                cur_row-=1



if __name__ == "__main__":
    cnt = 0
    ROW = 12
    COL = 6

    while True:
        visited = [[0] * COL for _ in range(ROW)]
        answers = []
        for i in range(ROW):
            for j in range(COL):
                tmp = []
                if not visited[i][j] and graph[i][j] != ".":
                    if get_same_color_cnt(graph[i][j], i, j) >= 4:
                        for row, col in tmp:
                            graph[row][col] = "."
                        answers+= tmp
        if len(answers) == 0:
            break

        pull_down_above_puyo()
        cnt+=1
    
    print(cnt)
