from collections import deque
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
square = [list(map(int, input().split())) for _ in range(N)]
directions = [[0,1], [1, 0], [-1, 0], [0, -1]]
answer = 0
cnt = 0

def find_melting_cheese():
    queue = deque()
    queue.append((0,0))
    visited = [[False] * M for _ in range(N)]
    visited[0][0] = True
    cheese_cnt = 0

    while queue:
        cur_row, cur_col = queue.popleft()
        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]

            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= M: continue
            if visited[next_row][next_col]: continue

            visited[next_row][next_col] = True
            if square[next_row][next_col] == 1:
                square[next_row][next_col] = 0
                cheese_cnt +=1
            else:
                queue.append((next_row, next_col))
    return cheese_cnt


while True:
    cheese = find_melting_cheese()
    if cheese == 0:
        break

    answer = cheese
    cnt+=1

print(cnt)
print(answer)