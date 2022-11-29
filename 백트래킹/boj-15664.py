N, M = map(int , input().split())

numbers = list(map(int, input().split()))

visited = [False] * N

answers = set()
def backtracking(depth, sequential):
    if depth == M:
        answers.add(tuple(sequential[1:]))
        return
    
    for idx in range(N):
        if not visited[idx] and sequential[-1] <= numbers[idx]:
            visited[idx] = True
            backtracking(depth+1, sequential + [numbers[idx]])
            visited[idx] = False
            
            
backtracking(0, [-1])
for answer in sorted(answers):
    print(*answer)