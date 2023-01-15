import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
op_cnts = list(map(int, input().split()))

min_value = sys.maxsize
max_value = -sys.maxsize

def backtracking(depth, cur_value):
    global min_value, max_value
    if depth == N:
        if cur_value < min_value:
            min_value = cur_value
        if cur_value > max_value:
            max_value = cur_value
        return
    
    for idx in range(len(op_cnts)):
        if op_cnts[idx]:
            op_cnts[idx]-=1
            if idx == 0: backtracking(depth+1, cur_value + numbers[depth])
            elif idx == 1: backtracking(depth+1, cur_value - numbers[depth])
            elif idx == 2: backtracking(depth+1, cur_value * numbers[depth])
            else: backtracking(depth+1, int(cur_value / numbers[depth]))
            op_cnts[idx]+=1

backtracking(1, numbers[0])
print(max_value)
print(min_value)