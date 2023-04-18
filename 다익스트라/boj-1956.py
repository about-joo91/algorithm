import sys
import heapq
input = sys.stdin.readline


V, E = map(int, input().split())
graph = [[ ] for _ in range(V+1)]
INF = int(10e9)
distances = [[INF] * (V+1) for _ in range(V+1)]
queue = []
for _ in range(E):
    start, end, dist = map(int, input().split())
    graph[start].append((dist, end))
    distances[start][end] = dist

    heapq.heappush(queue, [dist, start, end])


while queue:
    dist, start, end = heapq.heappop(queue)

    if start == end:
        print(dist)
        break

    if dist > distances[start][end]: continue

    for next_d, next_e in graph[end]:
        total_distance = dist + next_d
        if total_distance < distances[start][next_e]:
            distances[start][next_e] = total_distance
            heapq.heappush(queue, [total_distance, start, next_e])

else:
    print(-1)