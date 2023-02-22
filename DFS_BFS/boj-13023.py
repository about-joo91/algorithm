import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = [[ ] for _ in range(N)]
for _ in range(M):
	fir, sec = map(int, input().split())
	graph[fir].append(sec)
	graph[sec].append(fir)

def dfs(cur_node, depth):
	global answer
	if depth == 4:
		answer = True
		return
	visited[cur_node] = True
	for next_node in graph[cur_node]:
		if not visited[next_node]:
			dfs(next_node, depth+1)
			visited[next_node] = False

visited = [False] * N
answer= False
for i in range(N):
	dfs(i, 0)
	visited[i] = False
	if answer:
		break

print(1 if answer else 0)