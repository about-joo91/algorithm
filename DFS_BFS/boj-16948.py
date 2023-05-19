from collections import deque

N = int(input())
directions = [[-2, -1], [-2, 1], [0, -2], [0, 2], [2, -1], [2, 1]]
start_r, start_c, target_r, target_c = map(int, input().split())
distances = [[-1] * N for _ in range(N)]
queue = deque()
distances[start_r][start_c] = 0
queue.append((start_r, start_c))
while queue:
    cur_r, cur_c = queue.popleft()
    if cur_r == target_r and cur_c == target_c:
        print(distances[cur_r][cur_c])
        break
    for direction in directions:
        next_r = cur_r + direction[0]
        next_c = cur_c + direction[1]
        if next_r < 0 or next_r >= N or next_c < 0 or next_c >= N: continue
        if distances[next_r][next_c] != -1: continue
        distances[next_r][next_c] = distances[cur_r][cur_c] + 1
        queue.append((next_r, next_c))
else:
    print(-1)
