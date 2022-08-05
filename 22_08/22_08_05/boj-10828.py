import sys
iter_num = int(sys.stdin.readline())
stack = []
for _ in range(iter_num):
    operator = sys.stdin.readline().split()
    if operator[0] == 'push':
        stack.append(int(operator[1]))
    elif operator[0] == 'top':
        try:
            print(stack[-1])
        except:
            print(-1)
    elif operator[0] == 'pop':
        try:
            print(stack.pop())
        except:
            print(-1)
    elif operator[0] == 'size':
        print(len(stack))
    else:
        print(int(len(stack) == 0))