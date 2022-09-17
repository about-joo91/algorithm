import sys
input = sys.stdin.readline

M = int(input().rstrip())
S = set()

for _ in range(M):
    operators = input().rstrip().split()
    if len(operators) == 1:
        if operators[0] == "all":
            S = set(range(1, 21))
        else:
            S = set()
        continue
    operator, num = operators
    num = int(num)
    if operator == "add":
        S.add(num)
    elif operator == "check":
        print(int(num in S))
    elif operator == "remove":
        S.discard(num)
    elif operator == "toggle":
        if num in S:
            S.discard(num)
        else:
            S.add(num)