import sys
input = sys.stdin.readline
left_strings = list(input().rstrip())
right_strings = []
N = int(input())
for _ in range(N):
    operators = input().rstrip().split()
    operator = operators[0]
    if operator == "L":
        if left_strings: right_strings.append(left_strings.pop())
    elif operator == "D":
        if right_strings: left_strings.append(right_strings.pop())
    elif operator == "B":
        if left_strings: left_strings.pop()
    else:
        left_strings.append(operators[1])
print("".join(left_strings) + "".join(reversed(right_strings)))