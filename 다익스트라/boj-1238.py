import heapq
import sys
sys.stdin = open('', 'r')


def get_shortest_way_from_start(start, to):
    INF = int(10e9)
    distances = [INF] * (N+1)
    distances[start] = 0

    distance_check_queue = []
    heapq.heappush(distance_check_queue, (0, start))

    while distance_check_queue:
        cur_weight, cur_node = heapq.heappop(distance_check_queue)
        
        if distances[cur_node] != cur_weight: continue
        
        for next_weight, next_node in graph[cur_node]:
            cur_distance = distances[cur_node] + next_weight
            if distances[next_node] <= cur_distance: continue
            distances[next_node] = cur_distance
            heapq.heappush(distance_check_queue,(distances[next_node], next_node))
            
    return distances[to]



if __name__ == '__main__':

    N, M, start = map(int, input().split())

    graph = [[ ] for _ in range(N+1)]

    for _ in range(M):
        u, v, distance = map(int, input().split())
        
        graph[u].append((distance, v))

    total_distances = [0] * (N+1)

    for i in range(1, N+1):
        if i == start: continue
        total_distances[i] += get_shortest_way_from_start(start, i)
        total_distances[i] += get_shortest_way_from_start(i, start)

    print(max(total_distances))

