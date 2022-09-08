import sys
input = sys.stdin.readline
N, M = map(int, input().split())

numbers = list(map(int, input().split()))

sum_indexes = []
for _ in range(M):
    sum_indexes.append(list(map(int, input().split())))

prefix_sums = [0]
cur_sum = 0
for i in range(N):
    cur_sum += numbers[i]
    prefix_sums.append(cur_sum)

for i in range(M):
    sum_index = sum_indexes[i]
    print(prefix_sums[sum_index[1]] - prefix_sums[sum_index[0]-1])