N, M = map(int, input().split())

numbers = list(map(int , input().split()))

answers = set()

def backtracking(depth, sequential):
    if depth == M:
        answers.add(tuple(sequential[1:]))
        return
    
    for number in numbers:
        if sequential[-1] <= number:
            backtracking(depth+1, sequential+ [number])
            
backtracking(0, [-1])

for answer in sorted(answers):
    print(*answer)