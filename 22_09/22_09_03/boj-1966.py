from collections import deque
import sys


def get_cnt():
    global cnt
    while priarities:
        if priarities[0] == max(priarities):
            priarities.popleft()
            index = indexes.popleft()
            if index == target_index:
                return cnt
            cnt+=1
        else:
            priarities.rotate(-1)
            indexes.rotate(-1)

input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    length, target_index = map(int, input().split())
    priarities = deque(input().split())
    indexes = deque(list(range(length)))
    cnt = 1
    print(get_cnt())