import sys
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
graph = [list(input().rstrip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def can_move(row, col):
	if row < 0 or row >= R or col < 0 or col >= C:
		return False
	if graph[row][col] == '#' or visited[row][col]:
		return False
	return True


def bfs(s_r, s_c):
	queue = deque()
	queue.append((s_r, s_c))
	visited[s_r][s_c] = True
	wolf_count = 0
	sheep_count = 0
	while queue:
		cur_r, cur_c = queue.popleft()
		if graph[cur_r][cur_c] == 'v':
			wolf_count += 1
		elif graph[cur_r][cur_c] == 'k':
			sheep_count += 1
		for direction in directions:
			next_r = cur_r + direction[0]
			next_c = cur_c + direction[1]
			if can_move(next_r, next_c):
				visited[next_r][next_c] = True
				queue.append((next_r, next_c))
	return (wolf_count, sheep_count)


t_w_count = 0
t_s_count = 0
for i in range(R):
	for j in range(C):
		if visited[i][j]: continue
		wolf_count, sheep_count = bfs(i, j)
		if wolf_count < sheep_count:
			t_s_count += sheep_count
		else:
			t_w_count += wolf_count

print(t_s_count, t_w_count)
