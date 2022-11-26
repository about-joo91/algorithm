from collections import deque
import sys
sys.stdin = open('/Users/jujeonghan/Developer/camp/algorithm_study/DFS_BFS/test.txt','r')


directions = [
        [1, 0, 0], [-1, 0, 0],
        [0, -1, 0],[0, 0, -1],
        [0, 1, 0], [0, 0, 1]
        ]

while True:
    L, R, C = map(int, input().split())
    if L == R == C == 0: break
    building = []
    for _ in range(L):
        building.append([input() for _ in range(R)])
        input()

    distances= [[[-1] * C for _ in range(R)] for _ in range(L)]

    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == "S":
                    start = (i, j, k)
                    distances[i][j][k] = 0
                if building[i][j][k] == "E":
                    end = (i, j, k)


    queue = deque()
    queue.append(start)


    while queue:
        if queue[0] == end:
            time = distances[end[0]][end[1]][end[2]]
            print(f"Escaped in {time} minute(s).")
            break
        cur_height, cur_row, cur_col = queue.popleft()

        for direction in directions:
            next_height = cur_height+ direction[0]
            next_row = cur_row + direction[1]
            next_col = cur_col + direction[2]

            if next_height < 0 or next_height >= L or next_row < 0 or next_row >= R or\
                next_col < 0 or next_col >= C: continue
            if distances[next_height][next_row][next_col] != -1: continue
            if building[next_height][next_row][next_col] == "#": continue

            distances[next_height][next_row][next_col] = distances[cur_height][cur_row][cur_col] +1
            queue.append((next_height, next_row, next_col))
    else: print("Trapped!")

    

    
