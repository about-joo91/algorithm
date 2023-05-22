import sys
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for i in range(1, N + 1):
	node = int(input())
	graph[node].append(i)


def dfs(cur_node, cur_set):
	global results
	cur_set.add(cur_node)
	visited[cur_node] = True
	for next_node in graph[cur_node]:
		if next_node not in cur_set:
			dfs(next_node, cur_set.copy())
		else:
			results += list(cur_set)


results = []
visited = [False] * (N + 1)
for i in range(1, N + 1):
	if not visited[i]:
		dfs(i, set())

print(len(results))
for result in sorted(results):
	print(result)
