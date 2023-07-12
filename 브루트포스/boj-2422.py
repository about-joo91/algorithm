import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
LIMIT = 3
visited = [False] * (N+1)
miss_match_flavors = [[ ] for _ in range(N+1)]
for i in range(M):
    flavor1, flavor2 = map(int, input().rstrip().split())
    miss_match_flavors[flavor1].append(flavor2)
    miss_match_flavors[flavor2].append(flavor1)

def is_miss_match(next_flavor, answer):
    for miss_match_flavor in miss_match_flavors[next_flavor]:
        if miss_match_flavor in answer:
            return True
    return False

def backtracking(depth, answer, idx):
    global result
    if depth == LIMIT:
        result += 1
        return
    
    for i in range(idx, N+1):
        if visited[i]: continue
        if is_miss_match(i, answer): continue
        visited[i] = True
        backtracking(depth+1, answer + [i], i)
        visited[i] = False

result = 0
backtracking(0, [], 1)
print(result)