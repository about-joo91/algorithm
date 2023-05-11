import sys
sys.stdin = open('test.txt','r')

import sys
input = sys.stdin.readline
from collections import defaultdict

N, D, K, C = map(int, input().split())
dishes = [int(input()) for _ in range(N)]
left, right = 0, K-1
cur_types = defaultdict(int)
cur_types[C] +=1

for i in range(right+1):
    cur_types[dishes[i]]+=1

result = -int(1e9)

while left < N:

    result = max(len(cur_types), result)
    right = left + K
    unique_type = set()
    addable = True
    for idx in range(left, right):
        idx %= N
        unique_type.add(dishes[idx])
        if dishes[idx] == C: addable = False

    cnt = len(unique_type)
    if addable: cnt+=1
    max_type_cnt = max(max_type_cnt, cnt)
    left +=1

print(max_type_cnt)