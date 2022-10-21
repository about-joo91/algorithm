import heapq

def get_short_path(start):
    short_paths = []
    heapq.heappush(short_paths, (0, start))
    
    while short_paths:
        cur_distance, cur_node = heapq.heappop(short_paths)
        
        # 현재 거리가 최소값이 될 가능성이 없음
        if cur_distance > distances[cur_node]:
            continue
        # 그래프를 조회하면서 이동할 다음 위치값, 다음 거리값을 가져와 현재 거리값과 더한다음
        # 다음 위치값의 현재 저장된 거리값과 비교한 후 적다면 업데이트를 해주고 short_paths에 더해준다.
        for next_end, next_distance in graph[cur_node]:
            cost = cur_distance + next_distance
            if cost < distances[next_end]:
                distances[next_end] = cost
                heapq.heappush(short_paths,(cost, next_end))

N, D = map(int, input().split())
graph = [[] for _ in range(D+1)]
INF = int(10e9)
distances = [INF] * (D+1)

# 빈그래프에 최종거리 D까지 순회하면서 거리를 1로 초기화 해준다.
for i in range(D):
    graph[i].append((i+1, 1))

# 지름길 값도 그래프에 추가해서 최소값을 구할 수 있도록 한다.
for _ in range(N):
    start, end, distance = map(int, input().split())
    if end > D:
        continue
    graph[start].append((end, distance))
    
get_short_path(0)
print(distances[D])