from collections import deque
import sys
sys.stdin = open("" , "r")

N, M = map(int,input().split())
maze = [input() for _ in range(N)]
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
visited = [[0] * M for _ in range(N)]
JIHOON = 0
FIRE = 1

route_queue = deque()
for i in range(N):
    for j in range(M):
        if maze[i][j] == "J":
            jihoon_location= (i, j, JIHOON)
            visited[i][j] = 1
        elif maze[i][j] == "F":
            route_queue.append((i, j, FIRE))
            visited[i][j] = 1

route_queue.append(jihoon_location)

def check_jihoon_trail() -> int:
    while route_queue:
        cur_row, cur_col, _type = route_queue.popleft()

        if _type == JIHOON and (cur_row == 0 or cur_row == N-1 or cur_col == 0 or cur_col == M-1):
            return visited[cur_row][cur_col]
        
        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]

            if 0 > next_row or next_row >= N or 0 > next_col or next_col >= M: continue

            if maze[next_row][next_col] == "#": continue

            if visited[next_row][next_col]: continue

            visited[next_row][next_col] = visited[cur_row][cur_col] +1
            route_queue.append((next_row, next_col, _type))
    return -1


result = check_jihoon_trail()

print(result if result != -1 else "IMPOSSIBLE")