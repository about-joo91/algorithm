import sys
input = sys.stdin.readline

def add_one_to_initial_maxtrix(row,col):
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            initial_matrix[i][j] = initial_matrix[i][j] + 1

def change_matrix_value_to_zero_or_one():
    for i in range(N):
        for j in range(M):
            initial_matrix[i][j] = initial_matrix[i][j] % 2

def is_both_matrix_same():
    return initial_matrix == target_matrix

def get_change_count():
    cnt = 0
    for i in range(N-2):
        for j in range(M-2):
            if initial_matrix[i][j] % 2 != target_matrix[i][j]:
                add_one_to_initial_maxtrix(i, j)
                cnt+=1
    return cnt


if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    initial_matrix = [list(map(int, list(input().rstrip()))) for _ in range(N)]
    target_matrix = [list(map(int, list(input().rstrip()))) for _ in range(N)]

    change_count = get_change_count()


    change_matrix_value_to_zero_or_one()


    if is_both_matrix_same():
        print(change_count)
    else: print(-1)