import sys
import heapq

N = int(input())
M = int(input())
graph = [[ ] for _ in range(N)]

for i in range(N):
    paths = list(map(int, input().split()))
    graph[i].append(i)
    for j in range(N):
        if paths[j]:
            graph[i].append(j)
            graph[j].append(i)


def dijkstra(start, end):
    dist = [-1] * N
    dist[start] = 1
    queue = []
    heapq.heappush(queue, start)
    while queue:
        cur_node = heapq.heappop(queue)
        for next_node in graph[cur_node]:
            if dist[next_node] == -1:
                dist[next_node] = 1
                heapq.heappush(queue, next_node)

    return True if dist[end] == 1 else False

plans = list(map(int, input().split()))
for i in range(len(plans)-1):
    if not dijkstra(plans[i]-1, plans[i+1]-1):
        print("NO")
        sys.exit(0)
print("YES")

# from collections import deque
# plans = list(map(int, input().split()))
# for i in range(len(plans)-1):
#     queue = deque()
#     queue.append(plans[i]-1)
#     is_linked = False
#     visited = [False] * N
#     visited[plans[i]-1] = True
#     while queue:
#         cur_node = queue.popleft()

#         for next_node in graph[cur_node]:
#             if next_node == plans[i+1]-1:
#                 is_linked = True
#                 break
#             if visited[next_node]: continue
#             visited[next_node] = True
#             queue.append(next_node)
#     if is_linked: continue
#     else:
#         print("NO")
#         sys.exit(0)
# print("YES")
