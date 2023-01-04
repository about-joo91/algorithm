import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[ ] for _ in range(N+1)]
spanning_tree = [0] * (N+1)
priority_queue = []
cnt = 0
answer = 0

for _ in range(M):
    f_num, s_num, dist = map(int, input().split())

    graph[f_num].append((dist, s_num))
    graph[s_num].append((dist, f_num))

spanning_tree[1] = 1
for node in graph[1]:
    heapq.heappush(priority_queue, (node[0], 1, node[1]))

while cnt < N-1:
    cost, start_edge, end_edge = heapq.heappop(priority_queue)

    if spanning_tree[end_edge]: continue

    spanning_tree[end_edge] = 1
    cnt+=1
    answer += cost
    for next_node in graph[end_edge]:
        if not spanning_tree[next_node[1]]:
            heapq.heappush(priority_queue, (next_node[0], end_edge, next_node[1]))

print(answer)