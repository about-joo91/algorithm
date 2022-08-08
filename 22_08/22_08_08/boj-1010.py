import math
iter_num = int(input())
for _ in range(iter_num):
    N , M = map(int, input().split())
    print(math.comb(M, N))