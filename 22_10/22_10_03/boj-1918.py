import sys
input= sys.stdin.readline

infix = list(input().rstrip())
stack = []
answer = ""

for string in infix:
    if string.isalpha():
        answer += string
    else:
        if string == "(":
            stack.append(string)
        elif string == "*" or string == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                answer += stack.pop()
            stack.append(string)
        elif string == "+" or string == "-":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.append(string)
        elif string == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()
while stack:
    answer += stack.pop()
print(answer)