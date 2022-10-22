from bisect import bisect_left
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

names = []
conditions = []

for _ in range(N):
    name, condition = input().rstrip().split()
    
    names.append(name)
    conditions.append(int(condition))
    
for _ in range(M):
    cur_num = int(input().rstrip())
    # 조건 리스트 안에 cur_num이 위치할 값이 곧 index이다.
    idx = bisect_left(conditions, cur_num)
    print(names[idx])