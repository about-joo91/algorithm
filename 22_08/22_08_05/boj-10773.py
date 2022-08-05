import sys
iter_num = int(sys.stdin.readline())
stack = []
for _ in range(iter_num):
    num_now = int(sys.stdin.readline())
    if num_now == 0:
        stack.pop()
        continue
    stack.append(num_now)
if len(stack) ==0:
    print(0)
else:
    print(sum(stack))