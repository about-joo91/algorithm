from collections import deque
import sys
sys.stdin = open('/Users/jujeonghan/Developer/camp/algorithm_study/시뮬레이션/test.txt','r')

N, M = map(int, input().split())

maps = [list(map(int, input().split(' '))) for _ in range(N)]
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

zeros = []
viruses = []

one_cnt = 0


for i in range(N):
    for j in range(M):
        if maps[i][j] == 0:
            zeros.append((i, j))

        elif maps[i][j] == 1:
            one_cnt+=1

        elif maps[i][j] == 2:
            viruses.append((i, j))

if len(viruses) == 0:
    print(N*M - one_cnt)
    sys.exit(0)

if one_cnt == 0:
    print(3)
    sys.exit(0)

if len(zeros) == 0:
    print(0)
    sys.exit(0)

def bfs():
    visited = [[False] * M for _ in range(N)]
    for v_row, v_col in viruses:
        visited[v_row][v_col] = True

    cnt = 0
    queue = deque(viruses)
    while queue:
        cur_row, cur_col = queue.popleft()
        cnt+=1

        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]

            if 0 > next_row or next_row >= N or 0 > next_col or next_col >= M: continue

            if visited[next_row][next_col]: continue
            
            if maps[next_row][next_col] == 1: continue

            if maps[next_row][next_col] == 0:
                visited[next_row][next_col] = True
                queue.append((next_row, next_col))
    return cnt
                
answer = 0
back_tracking_visited = [[False] * M for _ in range(N)]

def backtracking(depth):
    global answer
    if depth == 3:
        virus_cnt = bfs()
        if answer < N * M - one_cnt - virus_cnt- 3:
            answer = N * M - one_cnt - virus_cnt- 3
        return

    for row, col in zeros:
        if not back_tracking_visited[row][col]:
            back_tracking_visited[row][col] = True
            maps[row][col] = 1
            backtracking(depth+1)
            back_tracking_visited[row][col] = False
            maps[row][col] = 0

backtracking(0)
print(answer)