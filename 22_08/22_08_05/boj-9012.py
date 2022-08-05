import sys
iter_num = int(sys.stdin.readline())

for _ in range(iter_num):
    parenthesis = list(sys.stdin.readline())
    result = 0
    for par in parenthesis:
        if par == '(':
            result += ord('(')
        elif par == ')':
            result -= (ord(')')-1)
        if result < 0:
            print('NO')
            break
    else:
        if result == 0:
            print('YES')
        else:
            print('NO')