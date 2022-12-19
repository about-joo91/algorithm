import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(9)]
zeros = []

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zeros.append((i,j))

def check_row(row, target):
    for j in range(9):
        if target == graph[row][j]:
            return False
    return True

def check_col(col, target):
    for i in range(9):
        if target == graph[i][col]:
            return False
    return True

def check_square(row,col, target):
    start_row = row // 3 * 3
    start_col = col // 3 * 3

    for i in range(start_row, start_row+3):
        for j in range(start_col, start_col+3):
            if graph[i][j] == target:
                return False
    return True

def backtracking(depth):
    if depth == len(zeros):
        for i in range(9):
            print(*graph[i])
        sys.exit(0)

    for i in range(1, 10):
        cur_row, cur_col = zeros[depth]
        if check_row(cur_row, i) and check_col(cur_col, i) and check_square(cur_row,cur_col, i):
            graph[cur_row][cur_col] = i
            backtracking(depth+1)
            graph[cur_row][cur_col] = 0


backtracking(0)
