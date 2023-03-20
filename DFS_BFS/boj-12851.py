import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
time_checker = [[-1, 0]] * 100001
queue = deque()

queue.append(N)
time_checker[N] = [0,1]
while queue:
    cur_location= queue.popleft()

    for next_location in [cur_location+1, cur_location*2, cur_location-1]:
        if next_location < 0 or next_location >= 100001: continue

        if time_checker[next_location][0] == -1:
            time_checker[next_location] = [time_checker[cur_location][0] +1, time_checker[cur_location][1]]
            queue.append(next_location)
        elif time_checker[next_location][0] == time_checker[cur_location][0] + 1:
            time_checker[next_location][1] += time_checker[cur_location][1]

for answer in time_checker[K]:
    print(answer)