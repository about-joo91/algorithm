N, M = map(int, input().split())

numbers = list(map(int, input().split()))

answers = set()

def backtracking(depth, sequential):
    if depth == M:
        answers.add(tuple(sequential))
        return
    
    for number in numbers:
        backtracking(depth+1, sequential + [number])

backtracking(0, [])
for answer in sorted(answers):
    print(*answer)