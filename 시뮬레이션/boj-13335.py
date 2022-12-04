from collections import deque
import sys
input = sys.stdin.readline

N, W, L = map(int, input().split())
trucks = deque(map(int, input().split()))
queue = deque([0] * (W-1))

time = 1
cur_weight = 0

while sum(queue) != 0 or len(trucks) != 0:

    if trucks and trucks[0] > L:
        trucks.popleft()
        continue
    if trucks and cur_weight + trucks[0] <= L:
        cur_truck = trucks.popleft()
        queue.append(cur_truck)
        cur_weight += cur_truck

    elif trucks and cur_weight + trucks[0] > L:
        queue.append(0)

    cur_weight -= queue.popleft()
    time +=1

print(time)