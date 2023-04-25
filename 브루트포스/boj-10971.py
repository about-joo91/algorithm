import sys
input = sys.stdin.readline

def backtracking(depth):
    global answer
    if depth == N:
        total_dist = 0
        city_orders = used + [used[0]]
        for idx in range(N):
            cur_dist = graph[city_orders[idx]][city_orders[idx+1]]
            total_dist += cur_dist if cur_dist != 0 else INF
        answer = min(answer, total_dist)
        return
    
    for i in range(N):
        if i not in used:
            used.append(i)
            backtracking(depth+1)
            used.pop()
        
N = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
used = []
INF = int(10e6)
answer = INF
backtracking(0)
print(answer)