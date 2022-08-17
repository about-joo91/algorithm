import sys
FIELD = 19
o_mok = [list(map(int, sys.stdin.readline().split())) for _ in range(FIELD)]
dr = [-1, 0, 1, 1]
dc = [1, 1, 1, 0]
answer = []
def bfs(row, col):  
    color = o_mok[row][col]
    for i in range(4):
        cnt = 1
        next_r = row + dr[i]
        next_c = col + dc[i]
        while 0<= next_r < FIELD and 0<= next_c < FIELD and o_mok[next_r][next_c] == color:
            cnt+=1
            if cnt == 5:
                if 0<= row - dr[i] < FIELD and 0<= col - dc[i] < FIELD and o_mok[row - dr[i]][col - dc[i]] == color:
                    break
                if 0<= next_r + dr[i] < FIELD and 0<= next_c + dc[i] < FIELD and o_mok[next_r + dr[i]][next_c + dc[i]] == color:
                    break
                print(color)
                print(row+1, col+1)
                sys.exit(0)
            next_r += dr[i]
            next_c += dc[i]
    return False
for i in range(FIELD):
    for j in range(FIELD):
        if o_mok[i][j] != 0:         
            bfs(i, j)
print(0)