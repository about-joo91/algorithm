import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))
N, M, R = map(int, input().rstrip().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
	start, end = map(int, input().split())
	graph[start].append(end)
	graph[end].append(start)
result = [0] * (N + 1)
def dfs(cur_node):
	global depth
	result[cur_node] = depth
	for next_node in sorted(graph[cur_node]):
		if result[next_node] == 0:
			depth +=1
			dfs(next_node)

depth = 1
dfs(R)
for node in result[1:]:
	print(node)
