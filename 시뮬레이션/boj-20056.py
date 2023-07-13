import sys
input = sys.stdin.readline

N, M, k = map(int, input().rstrip().split())
graph = [[[] for _ in range(N)] for _ in range(N)]
directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1],
              [-1, -1]]
fire_balls = []
for _ in range(M):
	r, c, m, s, d = map(int, input().rstrip().split())
	fire_balls.append((r - 1, c - 1, m, s, d))


def fire_ball_sum(r, c):
	t_m = t_s = 0
	even_cnt = odd_cnt = 0
	total_cnt = len(graph[r][c])
	while graph[r][c]:
		m, s, d = graph[r][c].pop()
		t_m += m
		t_s += s
		if d % 2 == 0:
			even_cnt += 1
		else:
			odd_cnt += 1

	if even_cnt == total_cnt or odd_cnt == total_cnt:
		return t_m, t_s, True
	return t_m, t_s, False


for _ in range(k):
	while fire_balls:
		r, c, m, s, d = fire_balls.pop()
		direction = directions[d]
		next_r = (r + s * direction[0]) % N
		next_c = (c + s * direction[1]) % N
		graph[next_r][next_c].append((m, s, d))

	for i in range(N):
		for j in range(N):
			if len(graph[i][j]) == 0: continue
			if len(graph[i][j]) == 1:
				fire_balls.append((i, j, *graph[i][j].pop()))
				continue
			count = len(graph[i][j])
			t_m, t_s, is_even = fire_ball_sum(i, j)
			start_num = 0 if is_even else 1
			for dir_idx in range(start_num, 8, 2):
				if t_m // 5 == 0: continue
				fire_balls.append((i, j, t_m // 5, t_s // count, dir_idx))

answer = 0
for fire_ball in fire_balls:
	answer += fire_ball[2]

print(answer)
