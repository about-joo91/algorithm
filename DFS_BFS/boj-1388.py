N, M = map(int, input().split())

house = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

def direction_of_type(type):
    if type == '-':
        return [0, 1]
    return [1, 0]
    
def dfs(cur_r, cur_c):
    visited[cur_r][cur_c] = True
    cur_type = house[cur_r][cur_c]
    direction = direction_of_type(cur_type)
    next_r = cur_r + direction[0]
    next_c = cur_c + direction[1]

    if next_r < 0 or next_r >= N or next_c < 0 or next_c >= M: return
    if visited[next_r][next_c]: return
    if house[next_r][next_c] != cur_type: return
        
    dfs(next_r, next_c)


count = 0

for i in range(N):
    for j in range(M):
        if visited[i][j]: continue
        count +=1
        dfs(i, j)

print(count)