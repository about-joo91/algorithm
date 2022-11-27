N, M = map(int, input().split())

numbers = list(map(int, input().split()))

answers = set()
used = []
visited = [0] * N

def backtracking(depth,cur_answer):
    if depth == M:
        answers.add(tuple(cur_answer))
        return
    
    for idx in range(N):
        if not visited[idx]:
            visited[idx] = 1
            backtracking(depth+1,cur_answer+[numbers[idx]])
            visited[idx] = 0
            
backtracking(0, [])
for answer in sorted(answers):
    print(*answer)