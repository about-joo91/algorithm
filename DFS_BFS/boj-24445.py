import sys
from collections import deque
input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
	start, end = map(int, input().rstrip().split())
	graph[start].append(end)
	graph[end].append(start)

visited = [0] * (N + 1)


def bfs(start):
	queue = deque()
	queue.append(start)
	count = 1
	visited[start] = count
	while queue:
		cur_node = queue.popleft()
		for next_node in sorted(graph[cur_node], reverse=True):
			if visited[next_node] != 0: continue
			count += 1
			visited[next_node] = count
			queue.append(next_node)


bfs(R)
for node in visited[1:]:
	print(node)
