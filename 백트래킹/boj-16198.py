N = int(input())
marbles = list(map(int, input().split()))


def calc_energy(idx):
	left = right = idx
	while visited[left]:
		left -= 1
	while visited[right]:
		right += 1
	return marbles[left] * marbles[right]


def dfs(depth, cur_answer):
	global answer
	if depth == N - 2:
		answer = max(answer, cur_answer)
		return

	for i in range(1, N - 1):
		if visited[i]: continue
		visited[i] = True
		energy = calc_energy(i)
		dfs(depth + 1, cur_answer + energy)
		visited[i] = False


answer = 0
visited = [False] * N
dfs(0, 0)
print(answer)