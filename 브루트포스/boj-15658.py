import sys

N = int(input())
numbers = list(map(int, input().split()))
operators = list(map(int, input().split()))

def get_operating_value(operator, number, depth):
    match operator:
        case 0:
            return number + numbers[depth+1]
        case 1:
            return number - numbers[depth+1]
        case 2:
            return number * numbers[depth+1]
        case 3:
            return int(number / numbers[depth+1])

max_value = -sys.maxsize
min_value = sys.maxsize
def dfs(depth, number):
    global max_value, min_value
    if depth == N-1:
        max_value = max(max_value, number)
        min_value = min(min_value, number)
        return
    
    for i in range(len(operators)):
        if operators[i] == 0: continue
        operators[i]-=1
        operating_value = get_operating_value(i, number, depth)
        dfs(depth+1, operating_value)
        operators[i]+=1

dfs(0, numbers[0])
print(max_value)
print(min_value)
