import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
INF = int(10e9)
rooms = [list(map(int, list(input().rstrip()))) for _ in range(N)]
distances = [[INF] * N for _ in range(N)]
directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def get_minimum_cnt_of_black_room():
    queue = []
    heapq.heappush(queue, (0, 0, 0))
    distances[0][0] = 0

    while queue:
        dist, cur_row, cur_col = heapq.heappop(queue)

        if dist > distances[cur_row][cur_col]: continue
        
        for direction in directions:
            next_row = cur_row + direction[0]
            next_col = cur_col + direction[1]

            if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N: continue
            
            next_dist = dist
            if rooms[next_row][next_col] == 0:
                next_dist +=1

            if next_dist < distances[next_row][next_col]:
                distances[next_row][next_col] = next_dist
                heapq.heappush(queue, (next_dist, next_row, next_col))
    
    return distances[N-1][N-1]

print(get_minimum_cnt_of_black_room())