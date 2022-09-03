from collections import deque
import sys
T = int(input())
for _ in range(T):
    N = int(input())
    cubes = deque(list(map(int, input().split())))
    stack = []
    i = 0
    while cubes:
        if cubes[i] >= cubes[(i+1)*-1]:
            value = cubes.popleft()
        elif cubes[i] < cubes[(i+1)*-1]:
            value = cubes.pop()
        if not stack or stack[-1] >= value:
            stack.append(value)
        else:
            print("No")
            break
    else:
        print("Yes")    