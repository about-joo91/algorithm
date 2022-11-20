from collections import deque
import sys

sys.stdin = open('/Users/jujeonghan/Developer/camp/algorithm_study/다익스트라/test.txt', 'r')
N = 6
M = 8
INF = int(10e6)
distances = [INF] * (N+1)
visited = [0] * (N+1)
distances[1] = 0

graph = [[ ] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    
    graph[a].append((b, c))

while True:
    idx = -1
    for i in range(1, N+1):
        if visited[i]: continue
        if idx == -1: idx = i
        elif (distances[i] < distances[idx]): idx = i

    print(idx)
    if idx == -1 or distances[idx] == INF:
        break
    visited[idx] = 1
    for next_node in graph[idx]:
        distances[next_node[0]] = min(distances[next_node[0]],distances[idx] + next_node[1] )


print(distances)

# while queue:
#     cur_node = queue.popleft()

#     for node in graph[cur_node]:
#         distances[node[0]] = min(distances[cur_node] + node[1], distances[node[0]])

#     min_node = -1
#     min_distance = INF
#     for i in range(2, len(distances)):
#         if min_distance > distances[i] and not visited[i]:
#             min_distance = distances[i]
#             min_node = i
#     if min_node == -1: break

#     visited[min_node] = 1
#     queue.append(min_node)


# print(distances)