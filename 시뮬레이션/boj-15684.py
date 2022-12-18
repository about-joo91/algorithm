import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())

maps = [[0] * N for _ in range(H)]
answer = int(10e9)

for _ in range(M):
    row, col = map(int, input().split())
    maps[row-1][col-1] = 1
    
def is_same_col_and_end_point():
    for cur_col in range(N):
        j = cur_col
        for i in range(H):
            if maps[i][j]:
                j +=1
            elif j > 0 and maps[i][j-1]:
                j -=1
        
        if j != cur_col: return False
    return True
    
def dfs(depth, r_idx):
    global answer
    if is_same_col_and_end_point():
        answer = min(answer, depth)
    if depth == 3 or depth >= answer:
        return
    else:
        for i in range(r_idx, H):
            for j in range(N-1):
                if maps[i][j] != 0 or maps[i][j+1] != 0: continue
                if j > 0 and maps[i][j-1] != 0: continue
                maps[i][j] = 1
                dfs(depth+1, r_idx)
                maps[i][j] = 0
                
dfs(0, 0)
if answer == int(10e9): print(-1)
else: print(answer)