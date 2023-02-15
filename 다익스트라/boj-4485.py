import heapq
import sys
input = sys.stdin.readline

directions= [[1, 0], [0, 1], [-1, 0], [0, -1]]
test_case = 1
while True:
    N = int(input())
    if N == 0: break
    graph = [list(map(int,input().split())) for _ in range(N)]
    costs = [[int(10e9)] * N for _ in range(N)]
    queue = []
    heapq.heappush(queue, (graph[0][0], 0, 0))
    costs[0][0] = 0

    while queue:
        cost, cur_row, cur_col = heapq.heappop(queue)

        if cur_row == N-1 and cur_col == N-1:
            print(f"Problem {test_case}: {costs[cur_row][cur_col]}")
            break

        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]

            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N: continue
            new_cost = cost + graph[next_row][next_col]
            if new_cost < costs[next_row][next_col]:
                costs[next_row][next_col] = new_cost
                heapq.heappush(queue, (new_cost, next_row, next_col))

    test_case+=1