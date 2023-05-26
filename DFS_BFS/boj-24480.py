import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

N, M, R = map(int, input().split())
graph = [[ ] for _ in range(N+1)]
visited = [0] * (N+1)
for _ in range(M):
	start, end = map(int, input().split())
	graph[start].append(end)
	graph[end].append(start)

def dfs(cur_node):
	global visited_depth
	visited_depth+=1
	visited[cur_node] = visited_depth

	for next_node in sorted(graph[cur_node], reverse=True):
		if visited[next_node] == 0:
			dfs(next_node)

visited_depth = 0
dfs(R)
for node in visited[1:]:
	print(node)
