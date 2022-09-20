import sys
input = sys.stdin.readline


N = int(input())
papers = [list(map(int, input().split()))]
minus = zero = plus = 0
def dfs(r, c, n):
    global minus, zero, plus

    number = papers[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if papers[i][j] != number:
                for partial_row in range(3):
                    for partial_col in range(3):
                        nr = r + partial_row * n//3
                        nc = c + partial_col * n//3
                        dfs(nr,nc, n//3)
                return
    match number:
        case -1:
            minus += 1
        case 1:
            plus += 1
        case 0:
            zero += 1

dfs(0,0,N)

print(f"{minus}\n{zero}\n{plus}")