# 메모리:311912KB 속도 1544ms
import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())
N_numbers = deque(map(int, input().rstrip().split()))
M_numbers = deque(map(int, input().rstrip().split()))

answer = []
while N_numbers and M_numbers:
    if N_numbers[0] < M_numbers[0]:
        answer.append(N_numbers.popleft())
    else:
        answer.append(M_numbers.popleft())
if N_numbers:
    answer += list(N_numbers)
else:
    answer += list(M_numbers)
print(*answer)


# 코드가 길어지는게 싫어서 사용했던 데크를 사용하지 않고 구현한다면
# 아래와 같이 구현된다. 메모리:185116KB 속도 : 2152ms

import sys
input = sys.stdin.readline

N, M = map(int,input().rstrip().split())
N_numbers = list(map(int, input().rstrip().split()))
M_numbers = list(map(int, input().rstrip().split()))

n = 0
m = 0

answer = []
while n < N or m < M:
    if n == N:
        answer.append(M_numbers[m])
        m+=1
    elif m == M:
        answer.append(N_numbers[n])
        n+=1
    else:
        if N_numbers[n] < M_numbers[m]:
            answer.append(N_numbers[n])
            n+=1
        else:
            answer.append(M_numbers[m])
            m+=1
print(*answer)