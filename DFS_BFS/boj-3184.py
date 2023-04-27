from collections import deque

R, C = map(int, input().split())
yard = [list(input()) for _ in range(R)]
directions = [[0,1], [1, 0], [-1, 0], [0, -1]]
visited = [[False] * C for _ in range(R)]
total_wolf_cnt = 0
total_sheep_cnt = 0

def find_sheep_and_wolf(r,c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    sheep_cnt = 0
    wolf_cnt = 0
    
    while queue:
        cur_r, cur_c = queue.popleft()

        for direction in directions:
            next_r = cur_r + direction[0]
            next_c = cur_c + direction[1]

            if next_r < 0 or next_r >= R or next_c < 0 or next_c >= C: continue
            if visited[next_r][next_c]: continue
            if yard[next_r][next_c] == "#": continue

            if yard[next_r][next_c] == "o": sheep_cnt +=1
            if yard[next_r][next_c] == "v": wolf_cnt +=1
            visited[next_r][next_c] = True
            queue.append((next_r, next_c))
    return (sheep_cnt, wolf_cnt)

for i in range(R):
    for j in range(C):
        if visited[i][j] and yard[i][j] == "#": continue
        sheep_cnt, wolf_cnt = find_sheep_and_wolf(i, j)
        if sheep_cnt > wolf_cnt:
            total_sheep_cnt += sheep_cnt
        else:
            total_wolf_cnt += wolf_cnt

print(total_sheep_cnt, total_wolf_cnt)