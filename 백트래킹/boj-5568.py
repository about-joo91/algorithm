N = int(input())
K = int(input())
numbers = [input() for _ in range(N)]
visited = [False] * N
answer = []


def back_trackting(cur_num, depth):
	if depth == K:
		answer.append(cur_num)
		return
	for i in range(N):
		if visited[i]: continue
		visited[i] = True
		back_trackting(cur_num + numbers[i], depth + 1)
		visited[i] = False


back_trackting("", 0)
print(len(set(answer)))
