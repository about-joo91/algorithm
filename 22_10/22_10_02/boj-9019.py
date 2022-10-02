import sys
from collections import deque
# input = sys.stdin.readline


T = int(input().rstrip())

def get_operator(start, end):
    queue = deque([(start, "")])
    visited = [False] * 10000
    
    while queue:
        cur_number, cur_operator = queue.popleft()
        visited[cur_number] = True
        
        D = (cur_number *2)% 10000
        if not visited[D]:
            if D == end:
                return cur_operator+"D"
            visited[D] = True
            queue.append((D, cur_operator+"D"))
        
        S = 9999 if cur_number == 0 else cur_number - 1
        if not visited[S]:
            if S == end:
                return cur_operator+"S"
            visited[S] = True
            queue.append((S, cur_operator+"S"))
        
        
        L = int(cur_number % 1000 * 10 + cur_number / 1000)
        if not visited[L]:
            if L == end:
                return cur_operator+"L"
            visited[L] = True
            queue.append((L , cur_operator + "L"))
            
        R = int(cur_number % 10 * 1000 + cur_number // 10)
        if not visited[R]:
            if R == end:
                return cur_operator+"R"
            visited[R] = True
            queue.append((R , cur_operator + "R"))
    

for _ in range(T):
    start, end = map(int, input().rstrip().split())
    
    print(get_operator(start, end))