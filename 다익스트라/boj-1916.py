import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[ ] for _ in range(N+1)]
for _ in range(M):
    fir_node, sec_node, dist = map(int, input().split())
    graph[fir_node].append((dist, sec_node))
    
queue = []

start, end = map(int, input().split())

heapq.heappush(queue,(0, start))

INF = int(10e9)
distances = [INF] * (N+1)
distances[start] = 0


while queue:
    dist, cur_node = heapq.heappop(queue)
    
    if distances[cur_node] != dist: continue
    
    for next_dist, next_node in graph[cur_node]:
        if dist + next_dist >= distances[next_node]:
            continue
        distances[next_node] = dist + next_dist
        heapq.heappush(queue, (dist + next_dist, next_node))
        

print(distances[end])