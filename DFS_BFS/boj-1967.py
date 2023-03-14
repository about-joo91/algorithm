import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def divided(cur_node, cur_dist):
    global answer
    left = right = 0
    for next_node, next_dist in graph[cur_node]:
        end_dist = divided(next_node, next_dist)
        if left <= right:
            left= max(left,end_dist)
        else:
            right = max(right, end_dist)

    answer = max(answer, left+right)
    return max(left+cur_dist, right+ cur_dist)

N = int(input())
graph = [[ ] for _ in range(N+1)]
for _ in range(N-1):
    start, end, dist = map(int, input().split())
    graph[start].append((end, dist))

answer = 0
divided(1, 0)
print(answer)