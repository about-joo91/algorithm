import sys
from collections import deque
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
bingo_board = [[0] * 5 for _ in range(5)]
bingo_cnt = 0
directions = [[1, 0], [0, 1], [1, 1], [-1, 1]]
weights = [1, -1]

def get_complete_line_cnt(r, c):
    cnt = 0
    for idx in range(4):
        if idx >= 2 and (r != c and (r+c) != 4): continue

        direction = directions[idx]
        queue = deque()
        queue.append((r, c, 1))
        visited = [[False] * 5 for _ in range(5)]
        visited[r][c] = True
        total_dist = 0
        while queue:
            cur_r, cur_c, dist = queue.popleft()
            for weight in weights:
                next_r = cur_r + (direction[0] * weight)
                next_c = cur_c + (direction[1] * weight)

                if next_r < 0 or next_r >= 5 or next_c < 0 or next_c >= 5:
                    if dist == 1: continue
                    total_dist += dist
                    continue
                if visited[next_r][next_c]: continue
                if bingo_board[next_r][next_c] == 0: continue

                visited[next_r][next_c] = True
                queue.append((next_r, next_c, dist+1))
        if total_dist >= 5:
            cnt+=1
    return cnt


def find_location_of_value(value, depth):
    if value in board[depth]:
        return (depth, board[depth].index(value))
    
    return find_location_of_value(value, depth+1)


notifications = [list(map(int, input().split())) for _ in range(5)]
answer = 0
for i in range(5):
    for j in range(5):
        notification = notifications[i][j]
        row, col = find_location_of_value(notification, 0)
        bingo_board[row][col] = 1
        complete_line_cnt = get_complete_line_cnt(row, col)
        answer += complete_line_cnt
        if answer >= 3:
            print((i * 5) + (j+1))
            sys.exit(0)

