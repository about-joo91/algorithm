N, M = map(int, input().split())

numbers = sorted(list(map(int, input().split())))

answers = []

def backtracking(depth):
    if depth == M:
        print(*answers)
        return
    for number in numbers:
        if not answers or (answers and answers[-1] <= number):
            answers.append(number)
            backtracking(depth+1)
            answers.pop()
        
backtracking(0)