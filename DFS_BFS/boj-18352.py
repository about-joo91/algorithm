import sys
from collections import deque
input = sys.stdin.readline

N, M, K, START = map(int, input().split())
graph = [[ ] for _ in range(N+1)]
INF = int(10e9)
distances = [INF] * (N+1)
for _ in range(M):
    start, end = map(int,input().split())
    graph[start].append(end)

def get_city_numbers_K_away_from_START():
    queue = deque()
    queue.append(START)
    distances[START] = 0

    while queue:
        cur_node = queue.popleft()

        for next_node in graph[cur_node]:
            if distances[next_node] > distances[cur_node] + 1:
                distances[next_node] = distances[cur_node] + 1
                queue.append(next_node)
    
    return [i for i, v in enumerate(distances) if v == K ]


city_numbers_K_away_from_START = get_city_numbers_K_away_from_START()
if city_numbers_K_away_from_START:
    for city_number in city_numbers_K_away_from_START:
        print(city_number)
else: print(-1)