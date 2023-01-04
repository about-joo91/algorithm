# from collections import deque

# N, SIS_LOC = map(int, input().split())

# visited = [False] * 100001

# def bfs(start):
#     queue = deque()
#     queue.append((start, 0))
#     visited[start] = True

#     while queue:
#         cur_loc, time = queue.popleft()

#         if cur_loc == SIS_LOC:
#             return time

#         next_loc = cur_loc * 2
#         if 0 <= next_loc < 100001 and not visited[next_loc]:
#             visited[next_loc] = True
#             queue.append((next_loc, time))
            
#         next_loc = cur_loc - 1
#         if next_loc >= 0 and not visited[next_loc]:
#             visited[next_loc] = True
#             queue.append((next_loc, time+1))

#         next_loc = cur_loc + 1
#         if 0 <= next_loc < 100001 and not visited[next_loc]:
#             visited[next_loc] = True
#             queue.append((next_loc, time+1))

# print(bfs(N))



import heapq

N, K = map(int, input().split())
INF = int(10e9)

def dijkstra():
    priority_queue = []
    fastest_times = [INF] * 100001
    fastest_times[N]= 0

    heapq.heappush(priority_queue,(0, N))

    while priority_queue:
        time, cur_loc = heapq.heappop(priority_queue)

        if time > fastest_times[cur_loc]:
            continue

        for next_loc, n_time in [(cur_loc-1, 1), (cur_loc +1, 1), (cur_loc*2, 0)]:
            
            sum_of_time = time + n_time

            if 0 <= next_loc < 100001 and sum_of_time < fastest_times[next_loc]:
                fastest_times[next_loc] = sum_of_time
                heapq.heappush(priority_queue, (sum_of_time, next_loc))

    return fastest_times[K]

print(dijkstra())

