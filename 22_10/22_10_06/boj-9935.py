import sys
input = sys.stdin.readline

string = list(input().rstrip())
bomb = input().rstrip()
stack = []
i = 0
while i < len(string):
    stack.append(string[i])
    i+=1
    if len(stack) >= len(bomb):
        check_string = "".join(stack[-len(bomb):])
        if check_string == bomb:
            cnt = 0
            while cnt < len(bomb):
                stack.pop()
                cnt+=1
if not stack:
    print("FRULA")
else:
    print("".join(stack))