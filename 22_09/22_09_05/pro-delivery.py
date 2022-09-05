
import heapq
import sys

def dijkstra(graph, distances):
    queue = []
    heapq.heappush(queue, (0 , 1))
    distances[1] = 0

    while queue:
        dist, node = heapq.heappop(queue)
        for next_node in graph[node]:
            if distances[next_node[0]] > dist + next_node[1]:
                distances[next_node[0]] = dist + next_node[1]
                heapq.heappush(queue, next_node[0], distances[next_node[0]]) 

def solution(N, roads, K):
    graph = [[ ] for _ in range(N+1)]
    distances = [sys.maxsize] * (N+1)

    for road in roads:
        graph[road[0]].append([road[1], road[2]])
        graph[road[1]].append([road[0], road[2]])

    dijkstra(graph, distances)
    answer = len(filter(lambda x : x >=K, distances))
    return answer