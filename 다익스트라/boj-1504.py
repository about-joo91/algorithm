import sys
import heapq

def dijkstra(start, end):
    distances = [INF] * (N+1)
    distances[start] = 0
    queue = []
    heapq.heappush(queue,(0, start))

    while queue:
        prev_dist, prev_node = heapq.heappop(queue)

        if distances[prev_node] != prev_dist: continue

        for cur_dist, cur_node in graph[prev_node]:
            next_dist = prev_dist + cur_dist
            if distances[cur_node] <= next_dist: continue
            distances[cur_node] = next_dist
            heapq.heappush(queue, (next_dist, cur_node))

    return distances[end]


N, E = map(int, input().split())
INF= int(10e9)
graph = [[ ] for _ in range(N+1)]
for _ in range(E):
    a, b, dist = map(int, input().split())
    graph[a].append((dist, b))
    graph[b].append((dist, a))


u, v = map(int, input().split())

first = dijkstra(1, u) + dijkstra(u, v) + dijkstra(v, N)
second = dijkstra(1, v) + dijkstra(v, u)+ dijkstra(u, N)

if first >= INF and second >= INF:
    print(-1)
else:
    answer = min(first, second)
    print(answer)