import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
maps = [list(input()) for _ in range(R)]
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

hedge_queue = deque()
water_queue = deque()
hedge_visisted = [[False] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if maps[i][j]== "S":
            hedge_queue.append((i, j, 0))
        elif maps[i][j] == "*":
            water_queue.append((i, j))

hedge_visisted[hedge_queue[0][0]][hedge_queue[0][1]] = True

while hedge_queue:
    water_cnt = len(water_queue)
    while water_queue and water_cnt:
        cur_w_r, cur_w_c = water_queue.popleft()
        for direction in directions:
            next_w_r = cur_w_r + direction[0]
            next_w_c = cur_w_c + direction[1]

            if next_w_r < 0 or next_w_r >= R or next_w_c < 0 or next_w_c >= C: continue
            if maps[next_w_r][next_w_c] == "*" or maps[next_w_r][next_w_c] == "D" or maps[next_w_r][next_w_c] == "X": continue
            water_queue.append((next_w_r, next_w_c))
            maps[next_w_r][next_w_c] = "*"
        water_cnt-=1
    
    
    hedge_cnt = len(hedge_queue)
    while hedge_queue and hedge_cnt:
        cur_h_r, cur_h_c, time = hedge_queue.popleft()
        for direction in directions:
            next_h_r = cur_h_r + direction[0]
            next_h_c = cur_h_c + direction[1]                
            
            if next_h_r < 0 or next_h_r >= R or next_h_c < 0 or next_h_c >= C: continue
            if hedge_visisted[next_h_r][next_h_c]: continue
            if maps[next_h_r][next_h_c] == "D":
                print(time+1)
                sys.exit(0)
            if maps[next_h_r][next_h_c] == ".":
                hedge_visisted[next_h_r][next_h_c] = True
                hedge_queue.append((next_h_r, next_h_c, time+1))
        hedge_cnt -= 1

print("KAKTUS")
                



