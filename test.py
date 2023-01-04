import sys
from collections import deque
sys.stdin = open('/Users/jujeonghan/Developer/camp/algorithm_study/test.txt','r')
N, SIS_LOC = map(int, input().split())

visited = [False] * 100001

def bfs(start):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        cur_loc, time = queue.popleft()

        if cur_loc == SIS_LOC:
            return time

        next_loc = cur_loc * 2
        if 0 <= next_loc < 100001 and not visited[next_loc]:
            visited[next_loc] = True
            queue.append((next_loc, time))

        next_loc = cur_loc - 1
        if next_loc >= 0 and not visited[next_loc]:
            visited[next_loc] = True
            queue.append((next_loc, time+1))

        next_loc = cur_loc + 1
        if 0 <= next_loc < 100001 and not visited[next_loc]:
            visited[next_loc] = True
            queue.append((next_loc, time+1))

        
        

print(bfs(N))