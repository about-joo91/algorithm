from collections import deque
import sys
input = sys.stdin.readline

def is_wall(row, col):
    return graph[row][col] == "#"


def get_location_after_move(row, col, direction):
    check_cnt = 0
    while graph[row + direction[0]][col + direction[1]] != "#" and graph[row][col] != "O":
        check_cnt+=1
        row += direction[0]
        col += direction[1]
    
    
    return row, col, check_cnt
    

def bfs(r_row, r_col, b_row, b_col):
    queue = deque()
    queue.append((r_row, r_col, b_row, b_col, 0))
    visited[r_row][r_col][b_row][b_col] = True
    while queue:
        cur_r_row, cur_r_col, cur_b_row, cur_b_col, cnt = queue.popleft()

        if cnt >= 10:
            break

        for direction in directions:
            n_r_row, n_r_col, r_cnt = get_location_after_move(cur_r_row, cur_r_col, direction)
            n_b_row, n_b_col, b_cnt = get_location_after_move(cur_b_row, cur_b_col, direction)

            if graph[n_b_row][n_b_col] == "O": continue
            if graph[n_r_row][n_r_col] == "O": return cnt+1

            if n_r_row ==n_b_row and n_r_col == n_b_col:
                if r_cnt > b_cnt:
                    n_r_row -= direction[0]
                    n_r_col -= direction[1]
                else:
                    n_b_row -= direction[0]
                    n_b_col -= direction[1]
            
            if not visited[n_r_row][n_r_col][n_b_row][n_b_col]:
                visited[n_r_row][n_r_col][n_b_row][n_b_col] = True
                queue.append((n_r_row, n_r_col, n_b_row, n_b_col, cnt+1))
    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [list(input()) for _ in range(N)]

    visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if graph[i][j] == "B":
                b_row, b_col = i, j
            elif graph[i][j] == "R":
                r_row, r_col = i, j

    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    print(bfs(r_row, r_col, b_row, b_col))