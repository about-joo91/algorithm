N, M = map(int, input().split())

numbers = sorted(list(map(int, input().split())))

answers = []
used = []

def backtracking(depth, start):
    if depth == M:
        print(*used)
        return
        
    for idx in range(start, N):
        number = numbers[idx]
        used.append(number)
        backtracking(depth+1, idx+1)
        used.pop()
            
backtracking(0, 0)