import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
times = [[-1, -1] for _ in range(100001)]

def can_move(next_loc):
    if next_loc < 0 or next_loc >= 100001: return False
    if times[next_loc][0] != -1 and times[next_loc][0] < times[cur_loc][0] +1: return False
    return True

times[N] = [0, -1]
queue = deque()
queue.append(N)
while queue:
    cur_loc = queue.popleft()
    
    if cur_loc == K:
        print(times[cur_loc][0])
        locations = []
        while cur_loc != -1:
            locations.append(cur_loc)
            cur_loc = times[cur_loc][1]
        print(*reversed(locations))
        break
    filtered_next_locs = list(filter(can_move,[cur_loc+1, cur_loc-1, cur_loc*2]))

    for next_loc in filtered_next_locs:
        times[next_loc] = [times[cur_loc][0]+1, cur_loc]
        queue.append(next_loc)