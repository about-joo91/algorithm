import sys
input = sys.stdin.readline

N = int(input().rstrip())

answer = 0
stack = []


for _ in range(N):
    building = int(input().rstrip())
    while stack and stack[-1] <= building:
        stack.pop()
        
    answer += len(stack)
    stack.append(building)
    
print(answer)