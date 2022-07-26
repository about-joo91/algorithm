from collections import deque
import sys

cur_su, sister = map(int, input().split())

queue = deque([])
visited =[False]* 100001
visited[cur_su] = True
queue.append([cur_su, 0])
directions = ['+1' , '-1', '*2']
while queue:
    cur_su, time = queue.popleft()
    if cur_su == sister:
        print(time)
        sys.exit(0)
    for direction in directions:
        n_su = eval(str(cur_su) + direction)
        n_time = time +1
        if 0 <= n_su <= 100000 and not visited[n_su]:
            visited[n_su] = True
            queue.append([n_su , n_time])
print(-1)