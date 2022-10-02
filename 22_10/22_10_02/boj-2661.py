import sys
sys.setrecursionlimit(int(1e9))
n = int(input())
answer = []

def backtracking(depth):
    for i in range(1, (depth//2) +1):
        if answer[-i:] == answer[-2*i:-i]: return -1
    if depth == n:
        print(''.join(map(str, answer)))
        return 0
    
    for i in range(1, 4):
        answer.append(i)
        if backtracking(depth+1) == 0:
            return 0
        answer.pop()

backtracking(0)