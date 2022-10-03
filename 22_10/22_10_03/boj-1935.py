import sys
input = sys.stdin.readline

N = int(input().rstrip())
postfix_expression = input().rstrip()
numbers = [input() for _ in range(N)]

stack = []
index = 0
for string in postfix_expression:
    if string.isalpha():
        stack.append(string)
        continue
    second = stack.pop()
    second = numbers[ord(second) - ord("A")] if type(second) == str else second
    first = stack.pop()
    first = numbers[ord(first) - ord("A")]if type(first) == str else first
    
    stack.append(eval(str(first) + string + str(second)))

print("{0:.2f}".format(stack[0]))