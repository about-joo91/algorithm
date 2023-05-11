import sys
input = sys.stdin.readline

N, D, K, C = map(int, input().split())
dishes = [int(input()) for _ in range(N)]
dishes += dishes[:K]

max_type_cnt = 0

for i in range(N):
    max_type_cnt = max(len(set(dishes[i:i+K] + [C])), max_type_cnt)

print(max_type_cnt)