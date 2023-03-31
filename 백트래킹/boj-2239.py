import sys
input = sys.stdin.readline

def can_write_target_in_square(r, c, target):
    init_r = r//3 * 3
    init_c = c//3 * 3

    for i in range(init_r, init_r+3):
        for j in range(init_c, init_c+3):
            if board[i][j] == target:
                return False
    return True


def can_write_target_in_row(r, target):
    for i in range(9):
        if board[r][i] == target:
            return False
    return True


def can_write_target_in_col(c, target):
    for i in range(9):
        if board[i][c] == target:
            return False
    return True


def print_board_when_numbers_are_filled(depth):
    if depth == len(zeros):
        for i in range(9):
            print("".join(list(map(str, board[i]))))
        sys.exit(0)
    
    cur_row, cur_col = zeros[depth]
    for i in range(1, 10):
        if can_write_target_in_square(cur_row, cur_col, i) and \
            can_write_target_in_row(cur_row, i) and \
            can_write_target_in_col(cur_col, i):
            board[cur_row][cur_col] = i
            print_board_when_numbers_are_filled(depth+1)
            board[cur_row][cur_col] = 0

if __name__ == "__main__":
    board = [list(map(int, list(input().rstrip()))) for _ in range(9)]
    zeros = []
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                zeros.append((i, j))

    print_board_when_numbers_are_filled(0)