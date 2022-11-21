import heapq
import sys
sys.stdin = open('', 'r')
N = int(input())
M = int(input())
graph = [[ ] for _ in range(N+1)]
for _ in range(M):
    u, v, cost = map(int, input().split())
    graph[u].append((cost, v))
    
start, end = map(int, input().split())
INF = int(10e9)
distances = [INF] *(N+1)
possible_road = []
pre_road = [0]* (N+1)
distances[start] = 0
heapq.heappush(possible_road, (0, start))

while possible_road:
    cur_weight, cur_node = heapq.heappop(possible_road)
    if distances[cur_node] != cur_weight: continue
    
    for next_weight, next_node in graph[cur_node]:
        next_distance = cur_weight + next_weight
        if next_distance >= distances[next_node]: continue
        distances[next_node] = next_distance
        heapq.heappush(possible_road, (next_distance, next_node))
        pre_road[next_node] = cur_node
            
print(distances[end])
cur_idx = end
road_stack = []
while cur_idx != start:
    road_stack.append(cur_idx)
    cur_idx = pre_road[cur_idx]
road_stack.append(cur_idx)
print(len(road_stack))
for road in reversed(road_stack):
    print(road, end=' ')