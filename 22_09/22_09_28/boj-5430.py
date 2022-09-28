import sys
from collections import deque
# input= sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    reverse_cnt = 0
    operators = input().rstrip()
    n = int(input().rstrip())
    numbers = deque(input().rstrip()[1:-1].split(','))
    if not n:
        numbers = deque()
    for operator in operators:
        if operator == "R":
            reverse_cnt += 1
        elif numbers and operator == "D":
            if reverse_cnt % 2 == 0:
                numbers.popleft()
            else:
                numbers.pop()
        else:
            print("error")
            break
    else:
        if reverse_cnt % 2 != 0:
            numbers.reverse()
        print("[" + ",".join(numbers) + "]")