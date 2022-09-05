import heapq
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [[ ] for _ in range(N+1)]
distances = [-1] * (N+1)

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    distances[start] = 0
    
    while queue:
        dist, now = heapq.heappop(queue)
        
        for next_node in graph[now]:
            if distances[next_node] == -1:
                distances[next_node] = dist +1
                heapq.heappush(queue, (distances[next_node] , next_node))

for _ in range(M):
    fir, sec = map(int, input().split())
    graph[fir].append(sec)
    graph[sec].append(fir)

dijkstra(1)
maximum_node = max(distances)
print(distances.index(maximum_node), maximum_node, distances.count(maximum_node))