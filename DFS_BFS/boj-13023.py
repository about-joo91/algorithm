import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

graph = [[ ] for _ in range(N)]
for _ in range(M):
	fir, sec = map(int, input().split())
	graph[fir].append(sec)
	graph[sec].append(fir)

def is_cur_node_linked_fourth_depth(cur_node, depth):
	global is_linked_fourth_depth
	if depth == 4:
		is_linked_fourth_depth = True
		return
	visited[cur_node] = True
	for next_node in graph[cur_node]:
		if not visited[next_node]:
			is_cur_node_linked_fourth_depth(next_node, depth+1)
			visited[next_node] = False

visited = [False] * N
is_linked_fourth_depth = False
for i in range(N):
	is_cur_node_linked_fourth_depth(i, 0)
	visited[i] = False
	if is_linked_fourth_depth:
		break

print(int(is_linked_fourth_depth))