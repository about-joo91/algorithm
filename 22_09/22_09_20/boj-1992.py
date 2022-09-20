N = int(input())
video = [list(map(int, (input()))) for _ in range(N)]
answer = ""
def dfs(r, c, n):
    global answer
    number = video[r][c]
    for i in range(r, r+n):
        for j in range(c, c+n):
            if video[i][j] != number:
                answer += "("
                for row_weight in range(2):
                    for col_weight in range(2):
                        nr = r + row_weight * n //2
                        nc = c + col_weight * n //2
                        dfs(nr, nc, n//2)
                answer += ")"
                return
    answer += str(number)
dfs(0,0,N)
print(answer)